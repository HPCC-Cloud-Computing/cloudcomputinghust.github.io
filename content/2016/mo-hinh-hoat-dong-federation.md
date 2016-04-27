Title: Mô hình hoạt động giữa client, Identity Provider và Service Provider
Slug: mo-hinh-hoat-dong-federation
Date: 2016-04-27 11:17
Author: Giáp Trần
Tags: keystone
Status: published


## Mô hình giả ngữ
```

+--------+						+-------+						+--------+
| Client |						|  IdP  |						|   SP   |
|        |						|       |						|        |
+--------+						+-------+						+--------+
	|---------- get Token -------->>|								|
	|								|								|
	|<<------- return Token --------|								|
	|								|								|
	|								|								|
	|---- get SAML2 assertion ---->>|								|
	|								|								|
	|<<-- return SAML2 assertion ---|								|
	|								|								|
	|								|								|
	|-------------- submit SAML2 assertion ----------------------->>|
	|								|								|
	|---------------- obtain unscope token ----------------------->>|
	|								|								|
	|<<------------------ return token access ----------------------|
	|								|								|
	|								|								|
	|-------------- use Service via token access ----------------_>>|
	|								|								|
```
## Mô hình kết nối
```

+--------+								+-------+						+--------+
| Client |								|  IdP  |						|   SP   |
|        |								|       |						|        |
+--------+								+-------+						+--------+
	|POST /v3/auth/tokens ---------------->>|								|
	|										|								|
	|<<------- return Token ----------------|								|
	|										|								|
	|										|								|
	|POST /v3/auth/OS-FEDERATION/saml2/ecp->|								|
	|										|								|
	|<<-- return SAML2 assertion -----------|								|
	|										|								|
	|										|								|
	|POST /Shibboleth.sso/SAML2/ECP -------------------------------------->>|
	|										|								|
	|GET /v3/OS-FEDERATION/identity_providers/keystone-idp/protocols/saml2/auth|
	|										|								|
	|<<------------------ return token access ----------------------|
	|										|								|
	|										|								|
	|GET /v3/OS-FEDERATION/domains  -------------------------------------->>|
	|GET /v3/OS-FEDERATION/project  -------------------------------------->>|
	|GET .......---------------------------------------------------------->>|
```
