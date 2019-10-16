---
layout: post
title: AWS budget alert setup (email and sms)
---

As a newbie to AWS who is pretty broke,
it is kind of important not to overspend due to own negligence or ignorance in the services that AWS employs,
for example not shutting down instances, leak keys etc.
Having a budget alert would quickly notify you in real time when you start spending real money in AWS that is more than you are willing to.

# Steps
1. Sign in to AWS management console


2. Under "Services" select "Billing" then under billing page select "Budgets", you'll be greeted by this page

   ![budget]({{ site.baseurl }}/images/budget.jpg)


3. Click "Create budget"


4. Select "Cost budget" as budget type before clicking "Set your budget to proceed"

   ![budget_type]({{ site.baseurl }}/images/budget-type.jpg)


5. In the next page, just fill in any budget name and cost you desired as circled below, the rest leave it as default values, scroll down the page and select "Configure alerts"

   ![setup_budget]({{ site.baseurl }}/images/setup-budget.jpg)


6. In this page fill in the email contacts to receive the alerts and tick the checkbox for "Notify via Amazon Simple Notification Service (SNS) topic"
   
   ![configure_alerts]({{ site.baseurl }}/images/configure-alerts.jpg)


7. A new textbox would appear, along with a new link "Manage your SNS topics" click on the link which should open in a new tab
   
   ![sns_link]({{ site.baseurl }}/images/sns-link.jpg)


8. You'll be brought to the Amazon SNS dashboard, select "Topics" from the side menu and click "Create topic"
   
   ![SNS_topics]({{ site.baseurl }}/images/sns-topics.jpg)


9. After being redirected to this page, fill in "Name" and "Display Name"
   
   ![SNS_details]({{ site.baseurl }}/images/sns-details.jpg)


10. Scroll down and select the drop down menu "Access policy - _optional_"
   
    ![dropdown_Access_policy]({{ site.baseurl }}/images/dropdown-access-policy.jpg)


11. Scroll to line 23 and delete the entire "Condition" chunk effectively from line 23-27, scroll down and select "Save changes"
   
    ![remove_condition]({{ site.baseurl }}/images/remove-condition.jpg)


12. You should be greeted by the following page, copy the arn which will begin in this format "arn:aws" followed by a long string of text and save it somewhere to refer back to later
   
    ![successful_topic_creation]({{ site.baseurl }}/images/successful-topic-creation.jpg)


13. Click "Create subscription" to continue the setup


14. From the "Protocol" selection menu, select "SMS", and for the Endpoint textbox fill in your number with your country code, when you are done click "Create subscription"
   
    ![create_subscription]({{ site.baseurl }}/images/create-subscription.jpg)


15. If every goes well you will be redirected to a page indicatiing that subscription has been successfully created
   
    ![successful_subscription]({{ site.baseurl }}/images/successful-subscription.jpg)


16. Go back to your previous tab that you left in step 7, and paste the arn you copied in step 12 into the "SNS Topic ARN" textbox
   
    ![paste_arn]({{ site.baseurl }}/images/paste-arn.jpg)


17. Click on "Create budget" and you are done!


That's honestly quite alot of steps and cerrtainly overwhelming if you are completely new to AWS but at least if it gives you a peace of mind when you go through day by day it is definitely worth it :))

