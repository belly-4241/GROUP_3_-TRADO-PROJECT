class Xpath_contact_us:
    QA_TRADO_URL = "https://qa.trado.co.il/"
    CONNECT = "//*[@id='root']/div/div[4]/div/span/i"
    CONTACT_US_LINK = "//a[contains(text(),'צור קשר')]"
    FRIST_NAME = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/span[1]/input[1]"
    SURNAME = "div.pages_pages div.pages_children.false:nth-child(3) div.contact_contactContainer:nth-child(2) div.contact_contactMain:nth-child(2) form.form_form.form_contactForm.contactForm div.form_items:nth-child(1) div.form_formItem.undefined.undefined.false.undefined:nth-child(2) span.input_input:nth-child(2) > input:nth-child(1)"
    EMAIL_CONTACT = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/span[1]/input[1]"
    TELEPHONE = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/span[1]/input[1]"
    REFERANCE_MESSAGE = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[5]/textarea[1]"
    SEND_BUTTON = "form_submitBtn"
    ASSERTION_SUCCESFULLY = "//div[contains(text(),'הפרטים נקלטו בהצלחה')]"


    ### assertion Error message
    SUCCESSFULLY_MESSAGE = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[3]"
    ERROR_FIRST_NAME = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]"
    ERROR_SURNAME = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]"
    ERROR_EMAIL = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]"
    ERROR_PHONE_NUMBER = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]"
    ERROR_MESSAGE = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[5]/div[1]"
    PHONE_INVALID = "div.pages_pages div.pages_children.false:nth-child(3) div.contact_contactContainer:nth-child(2) div.contact_contactMain:nth-child(2) form.form_form.form_contactForm.contactForm div.form_items:nth-child(1) div.form_formItem.undefined.undefined.false.undefined:nth-child(4) > div.form_note:nth-child(3)"