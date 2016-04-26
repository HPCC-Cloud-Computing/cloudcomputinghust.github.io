Title: Cấu hình Federation trong Keystone với bản phát hành Liberty.
Slug: cai-dat-keystone-to-keystone-federation
Date: 2016-04-25 20:30
Author: Giáp Trần
Tags: keystone
Status: published

Từ phiên bản v3 của Keystone. Đã hỗ trợ thêm phần Federation.
Trong bài hướng dẫn hôm nay, sử dụng 2 máy ảo Ubuntu 14.04 LTS chạy Devstack (stable/liberty).
Hai máy có cùng 1 mạng, để có thể kết nối với nhau.

- keystone.sp: 1 máy ảo được xem là SP (Service Provider). Được cài đặt các project cơ bản của OpenStack.
- keystone.idp: Máy ảo còn lại được xem là IdP (Identity Provider). Được cài đặt mỗi Keystone project.

## Kích hoạt Keystone V3 trong devstack/local.conf
```
[[local|localrc]]
...
ENABLE_IDENTITY_V2=False
```

## Cấu hình Keystone như một Identity Provider
- Cài đặt các gói phụ thuộc
```
sudo apt-get install xmlsec1  
sudo pip install pysaml2  
```

- Thêm tính năng sinh ra SAML assertions

Cấu hình trong nhãn [saml] tại ```/etc/keystone/keystone.conf```
```
[saml]
certfile=/etc/keystone/ssl/certs/ca.pem  
keyfile=/etc/keystone/ssl/private/cakey.pem  
idp_entity_id=http://keystone.idp/v3/OS-FEDERATION/saml2/idp  
idp_sso_endpoint=http://keystone.idp/v3/OS-FEDERATION/saml2/sso  
idp_metadata_path=/etc/keystone/keystone_idp_metadata.xml  
```
- Sinh ra khoá và chứng chỉ cho kết nối HTTPS
```
keystone-manage ssl_setup
```
- Sinh IdP metadata
```
keystone-manage saml_idp_metadata > /etc/keystone/keystone_idp_metadata.xml  
```
- Khởi động lại dịch vụ web apache2
```
sudo service apache2 restart  
```
## Cấu hình Keystone như một Service Provider
- Kích hoạt xác thực bằng SAML2
```
[auth]
methods = external,password,token,oauth1,saml2
saml2 = keystone.auth.plugins.mapped.Mapped  
```
- Cài đặt và cấu hình Shibboleth SP
```
sudo apt-get install libapache2-mod-shib2  
```
Thêm dòng WSGIScriptAliasMatch vào <VirtualHost *:5000> trong ```/etc/apache2/sites-available/keystone.conf```
```
<VirtualHost *:5000>
    WSGIScriptAliasMatch ^(/v3/OS-FEDERATION/identity_providers/.*?/protocols/.*?/auth)$   /usr/local/bin/keystone-wsgi-public/$1
...
```
Và thêm đoạn sau vào cuối tập tin ```/etc/apache2/sites-available/keystone.conf```
```
<Location /Shibboleth.sso>
    SetHandler shib
</Location>

<LocationMatch /v3/OS-FEDERATION/identity_providers/.*?/protocols/saml2/auth>
    ShibRequestSetting requireSession 1
    AuthType shibboleth
    ShibExportAssertion Off
    Require valid-user
</LocationMatch>
```
- Cập nhật ```/etc/shibboleth/attribute-map.xml```

```
<Attributes xmlns="urn:mace:shibboleth:2.0:attribute-map" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	<Attribute name="openstack_user" id="openstack_user"/>  
	<Attribute name="openstack_roles" id="openstack_roles"/>  
	<Attribute name="openstack_project" id="openstack_project"/>  
	....

```
- Cập nhật Keystone IdP entityID và MetadataProvider ```/etc/shibboleth/shibboleth2.xml```
```
<SSO entityID="https://keystone.idp/v3/OS-FEDERATION/saml2/idp">  
    SAML2 SAML1
</SSO>

<MetadataProvider type="XML" uri="https://keystone.idp/v3/OS-FEDERATION/saml2/metadata"/>  
```

- Sinh khoá và khởi động lại dịch vụ
```
sudo shib-keygen  
sudo a2enmod shib2  
sudo service apache2 restart  
```

## Đăng ký thông tin với nhau
Để SP và IdP có thể hiểu và trao đổi thông tin.

### Đắng ký IdP trong SP
- Tạo đối tượng SP trong IdP
```
import os

from keystoneclient import session as ksc_session  
from keystoneclient.auth.identity import v3  
from keystoneclient.v3 import client as keystone_v3

try:  
    # Used for creating the ADMIN user
    OS_PASSWORD = os.environ['OS_PASSWORD']
    OS_USERNAME = os.environ['OS_USERNAME']
    # This will vary according to the entity:
    # the IdP or the SP
    OS_AUTH_URL = os.environ['OS_AUTH_URL']
    OS_PROJECT_NAME = os.environ['OS_PROJECT_NAME']
    OS_DOMAIN_NAME = os.environ['OS_DOMAIN_NAME']
except KeyError as e:  
    raise SystemExit('%s environment variable not set.' % e)

def client_for_admin_user():  
    auth = v3.Password(auth_url=OS_AUTH_URL,
                       username=OS_USERNAME,
                       password=OS_PASSWORD,
                       user_domain_name=OS_DOMAIN_NAME,
                       project_name=OS_PROJECT_NAME,
                       project_domain_name=OS_DOMAIN_NAME)
    session = ksc_session.Session(auth=auth)
    return keystone_v3.Client(session=session)

# Used to execute all admin actions
client = client_for_admin_user()  

def create_sp(client, sp_id, sp_url, auth_url):  
        sp_ref = {'id': sp_id,
                  'sp_url': sp_url,
                  'auth_url': auth_url,
                  'enabled': True}
        return client.federation.service_providers.create(**sp_ref)

print('\nCreate SP')  
create_sp(client,  
          'keystone.sp',
          'http://keystone.sp:5000/Shibboleth.sso/SAML2/ECP',
          'http://keystone.sp:5000/v3/OS-FEDERATION/identity_providers/'
          'keystone-idp/protocols/saml2/auth')


```
### Đắng ký IdP trong SP

 - Tạo domain1
 - Tạo group1
 - Tạo role Member
 - Gắn role Member tới domain1 trong group1
 - mapping người dùng remote tới local
 - Đăng ký identity provider
 - Đăng ký giao thức trao đổi

```
import os
oup1
from keystoneclient import session as ksc_session  
from keystoneclient.auth.identity import v3  
from keystoneclient.v3 import client as keystone_v3

try:  
    # Used for creating the ADMIN user
    OS_PASSWORD = os.environ['OS_PASSWORD']
    OS_USERNAME = os.environ['OS_USERNAME']
    # This will vary according to the entity:
    # the IdP or the SP
    OS_AUTH_URL = os.environ['OS_AUTH_URL']
    OS_PROJECT_NAME = os.environ['OS_PROJECT_NAME']
    OS_DOMAIN_NAME = os.environ['OS_DOMAIN_NAME']
except KeyError as e:  
    raise SystemExit('%s environment variable not set.' % e)

def client_for_admin_user():  
    auth = v3.Password(auth_url=OS_AUTH_URL,
                       username=OS_USERNAME,
                       password=OS_PASSWORD,
                       user_domain_name=OS_DOMAIN_NAME,
                       project_name=OS_PROJECT_NAME,
                       project_domain_name=OS_DOMAIN_NAME)
    session = ksc_session.Session(auth=auth)
    return keystone_v3.Client(session=session)

# Used to execute all admin actions
client = client_for_admin_user()  

def create_domain(client, name):  
    try:
         d = client.domains.create(name=name)
    except:
         d = client.domains.find(name=name)
    return d

def create_group(client, name, domain):  
    try:
         g = client.groups.create(name=name, domain=domain)
    except:
         g = client.groups.find(name=name)
    return g

def create_role(client, name):  
    try:
        r = client.roles.create(name=name)
    except:
        r = client.roles.find(name=name)
    return r

print('\nCreating domain1')  
domain1 = create_domain(client, 'domain1')

print('\nCreating group1')  
group1 = create_group(client, 'group1', domain1)

print('\nCreating role Member')  
role1 = create_role(client, 'Member')

print('\nGrant role Member to group1 in domain1')  
#client.roles.grant(role1, group=group1, domain=domain1, os_inherit_extension_inherited=True)
client.roles.grant(role1, group=group1, domain=domain1)

print('\nList group1 role assignments')  
client.role_assignments.list(group=group1)  
def create_mapping(client, mapping_id, rules):  
    try:
        m = client.federation.mappings.create(
            mapping_id=mapping_id, rules=rules)
    except:
        m = client.federation.mappings.find(
            mapping_id=mapping_id)
    return m

print('\nCreating mapping')  
rules = [  
{
    "local": [
        {
            "user": {
                "name": "federated_user"
            },
            "group": {
                "id": group1.id
            }
        }
    ],
    "remote": [
        {
            "type": "openstack_user",
            "any_one_of": [
                "user1",
                "admin"
            ]
        }
    ]
}
]

mapping1 = create_mapping(client, mapping_id='keystone-idp-mapping', rules=rules)

def create_idp(client, id, remote_id):  
    idp_ref = {'id': id,
               'remote_ids': [remote_id],
               'enabled': True}
    try:
        i = client.federation.identity_providers.create(**idp_ref)
    except:
        i = client.federation.identity_providers.find(id=id)
    return i

def create_protocol(client, protocol_id, idp, mapping):  
    try:
        p = client.federation.protocols.create(protocol_id=protocol_id,
                                               identity_provider=idp,
                                               mapping=mapping)
    except:
        p = client.federation.protocols.find(protocol_id=protocol_id)
    return p


print('\nRegister keystone-idp')  
idp1 = create_idp(client, id='keystone-idp',  
                  remote_id='https://keystone.idp/v3/OS-FEDERATION/saml2/idp')

print('\nRegister protocol')  
protocol1 = create_protocol(client, protocol_id='saml2', idp=idp1,  
                            mapping=mapping1)


```

## Sử dụng script cài đặt tự động
Tải về [Tại đây](http://cloudcomputinghust.github.io/files/k2k-auto-config.zip)
```
├── auto-idp
│   ├── auto.sh
│   ├── insert_keystone.py
│   └── setup_k2k_idp.py
├── auto-sp
│   ├── auto.sh
│   ├── configure_shibboleth.py
│   ├── setup_k2k_sp.py
│   ├── update_apache_conf.py
│   └── update_keystone_conf.py
└── federated-login.sh
```

Thêm IP của các host vào /etc/hosts của mỗi máy ảo

VD:
```
192.168.1.2     keystone.idp
192.168.1.3     keystone.sp
```

- Trên host SP
```
export DEVSTACK=/thucmuc_devstack
cd auto-sp
./auto.sh
```
- Trên host IdP
```
export DEVSTACK=/thucmuc_devstack
cd auto-idp
./auto.sh
```

- test hoạt động

Trên host của IdP
```
cd /thucmuc_devstack
. openrc admin admin
# cd /k2k-auto-config-thu-muc
./federated-login.sh
```

### _Tài liệu tham khảo_
_[it-is-time-to-play-with-keystone-to-keystone-federation-in-kilo](http://blog.rodrigods.com/it-is-time-to-play-with-keystone-to-keystone-federation-in-kilo/)_
