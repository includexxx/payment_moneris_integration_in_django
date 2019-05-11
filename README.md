## This is my first django project
### Basic implemntation of Moneris for use with website
### when a sale order is created you can use moneris to pay the sale order
* You can setup a  new moneris accunt in http://127.0.0.1:8000/moneris/new
* You can see all account  http://127.0.0.1:8000/moneris/
* You can see all sale orders in http://127.0.0.1:8000/sale
* You can careate a sale  order in http://127.0.0.1:8000/sale/new


---
Setting up a developer account in Moneris.
For setting up the Moneris developer account, please follow the below steps:
---

---
Go to https://esqa.moneris.com/mpg/index.php
Log in using the credentials shown in the page
![moneris_1](https://user-images.githubusercontent.com/33756156/57568541-9df3b400-740a-11e9-9674-46a5554d7d0a.png)


---

From the dashboard, go to Admin -> Hosted Paypage Config and click on Generate a New Configuration button . Please note that there are configurations of other developers/users listed 
below the button, do not edit or delete those configurations.


After clicking on Generate a New Configuration button, you will get a ps_store_id and hpp_key for your developer account and a warning message like below:
![2](https://user-images.githubusercontent.com/33756156/57568559-fa56d380-740a-11e9-8b02-f76f034d78eb.png)


This configuration is currently flagged as temporary and will be deleted in 15 minutes.
To confirm this configuration please click 'Save Changes' below.
* ps_store_id: BBMQCtore3
* hpp_key: hp2MAP$JFRUS

* Then under Basic Configurations enter a description about your account or website.
* Then select a transaction type. By default, it will be 'Purchase'.
* Select the Payment Methods you need. For example, Credit cards, Gift cards etc.
* NOTE: Different payment types require extra coding to handle the transaction response and create a receipt.
* Then select the Response method and enter Approved URL and Declined URL. After a successful transaction the Moneris payment gateway will redirect to the Approved URL you have specified and if the transaction is declined, it will redirect to the Declined URL.


Then save the changes, now your developer account is ready.

For integrating your Moneris payment gateway account with website you can use the following details:
![3](https://user-images.githubusercontent.com/33756156/57568607-9385ea00-740b-11e9-9bb7-7e93c6ae54fb.png)

Response Method: Sent to your server as a POST
Approval URL: https://SITEURLHERE/moneris/payment/validate
Declined URL: https://SITEURLHERE/moneris/payment/validate
Use "Enhanced Cancel" Enabled
Use "Response Fallback" Disabled
### Under Configure Response Fields, ECI and txn_number Enabled.
### Under security features, Transaction Verification Enabled, and set to be displayed as key/value pairs on moneris's server.
![4](https://user-images.githubusercontent.com/33756156/57568629-f5deea80-740b-11e9-965b-5c226b3163ee.png)
