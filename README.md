# Automated Phishing Cyber Awareness Training

What is this here to accomplish?
	- Sends phishing email mimicing the newest type of phishing structure
	- Will only be via email no sms or over the phone
		- Clone Phishing:
			- A phishing attack that uses a legitimate email from a trusted source, but modifies the content with malicious links or attachments.

		- Business Email Compromise (BEC):
			- Phishing attacks that target businesses by impersonating company executives or vendors to request payments or sensitive information

	- Challenges
		- Mimicing the email sent from
		- Hyperlinking links for the pwned website
		- Training of real phishing emails from categories above
			- primarily focus will be on BEC and clone

	- TO DO:
		- making website for hyperlink to route to
			- website will have "YOU HAVE BEEN PHISHED/PWNED" and how to look out for these types
			of emails in a general context
			- based on the employee "class" or level of authority different ramifications are applied being an awareness class especially if it is not the first time the link was interacted with
		- training model to produce the phishing emails to look "real"

model: https://huggingface.co/heliart/PhishingEmailGeneration
templates: https://caniphish.com/free-phishing-test/phishing-email-templates
framework implementation (stretch goal): https://getgophish.com/