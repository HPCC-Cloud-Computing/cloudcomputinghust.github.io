Title: Trustworthy cloud platform service idea
Slug: trustworthy-cloud-platform-service-idea
Date: 2016-05-21 11:26
Author: Giáp Trần
Tags: keystone,federation,security
Status: published

#Cloud Security

##Preface

Cloud, it is not only concept. Cloud is a platform that is mentioned and grow very powerful years recently. A simple website or anyone complex services in Internet that you have used. It could be ran in Cloud platform.

When there have many applications, services in Cloud. Beside strength that Cloud bring. The issue of security information and secure Cloud service like?

## STATISTICS IN 2015
### Cloud applications

![apps-cloud.png](http://cloudcomputinghust.github.io/images/apps-cloud.png)

- Web applications 43%
- Communitaion apps 39%
- Sales and maketing 30%

### Data in the Cloud
Email is the most frequently stored corporate information in the cloud **(45%)**, followed by sales & marketing data **(42%)**, intellectual property **(38%)** and customer data **(31%)**. Few organizations storesensitive financial data **(19%)** or employee healthcare data **(8%)** in the cloud.

![data-cloud.png](http://cloudcomputinghust.github.io/images/data-cloud.png)


## ISSUE
At time Cloud appear, the computing resources and availblity are top concern. When Cloud has became platform to companys, users. Information security issues are put on top.
Many solution are given to limited, prevent the unauthorized access from hacker external.

But, data will be safe with Cloud provider?
Whether there exists a risk of losing safe security: from infrastructure, from network environment, from the staffs.. comes within the provider

**_“Do you trust an external third party with your sensitive data?”_**

This is the primary concern for companies that are joining the gold rush that is Cloud Computing.
The most common way to establish trust between a Cloud User (Data Controllers) and a Cloud Provider (Data Processors) is by establishing a Service Level Agreement (SLA) and auditing.

![issue.png](http://cloudcomputinghust.github.io/images/issue.png)

**Even if the Cloud provider is audited, the current situation introduces several serious security risks:**

1. As soon as the IT operations are moved into the Cloud the User loses control over it.
Example:  if data are uploaded into the Cloud (i.e. into a virtual machine’s
file system) the Provider always can accessed and modify it.
2. Even if the Cloud Provider is bind with SLA there are threats of disclosing customer’s
security sensitive data and computations inside the Cloud. Specifically malicious insiders
(e.g. Cloud administrators) represent a significant concern.
3. Security of the Cloud infrastructure has direct impact on the security of the other above layered levels, namely platforms and software

**To resolve the this security problems, we need to have answer for question:**

_“How do users are allowed to use cloud resources without the disclosure of sensitive information (data, applications/funcitons/workflow) for cloud providers. But at the same time allow the cloud provider to manage cloud infrastructure safely and effectively?”_

## IDEA
![idea.png](http://cloudcomputinghust.github.io/images/idea.png)

- Cloud User:

Do not provide authentication data directly Cloud Provider.

- Cloud Provider:

Do not know who is the owner of the data.

- Trust Sevice:

 **With User:** The service that users trusted to provide the personal information, and through this service to use the resources from the cloud provider, without knowing the resource is in any provider.

 **With Provider:** Do not know who your customers are, all customers will be transferred by this service a certain identity.
![idea-1.png](http://cloudcomputinghust.github.io/images/idea-1.png)
