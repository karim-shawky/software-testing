from pydoc_data.topics import topics
from selenium.webdriver.common.by import By

class StartingPageLocators(object):
    SIGN_UP_BY_PHONE_OR_EMAIL = (By.LINK_TEXT,"Sign up with a phone number or email")
    SIGN_IN = (By.LINK_TEXT,"Sign in")
    SIGN_IN_WITH_APPLE = (By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[2]")
    SIGN_IN_WITH_GOOGLE = ("/html/body/div/div/div[2]")
    
    
class SignInLocators(object):
    INSERT_UR_INFO = "text"
    NEXT_BUTTON = (By.XPATH,"//span[contains(text(),'Next')]")
    ALERT_MSG =("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
    
class SignUpLocators(object):
    NEXT_BUTTON = (By.XPATH,"//div[@class='css-1dbjc4n r-kemksi r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][normalize-space()='Next']")
    NAME_TEXTBOX =   "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    PHONE_TEXTBOX = "phone_number"  #NAME //div[@class='css-1dbjc4n r-1n7yuxj']//div[1]//label[1]//div[1]//div[2]
    MONTH         = "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-1nao33i r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"
    YEAR            = "SELECTOR_15"
    ERROR_MSG       = "//span[normalize-space()='Please enter a valid phone number.']" #XPATH
    EXPECTED_MSG    = "Please enter a valid phone number."
    WRONG_NAMEX50   ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    NEXT_CREATE_ACCOUNT ="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/a[1]/div[1]/p[1]"
    NEXT_PAGE_NEXT ="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]"
    EMAIL_TEXTBOX ="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[2]"
    EXPECTED_MSG_EMAIL="Please enter a valid email."
    EMAIL_TEXT="Email"
    EMAIL_TEXT_LOC='Div[id="placeholder"]'
    
class Passwordlocarors(object):
    PASSWORD_TEXTBOX= "password"  #NAME
    FORGET_PASSWORD = "//span[contains(text(),'Forgot password?')]" #XPATH
    LOGIN_BUTTON = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"
    FORGET_PASSWORD_TEXT = "Forgot password?"

class Settings_Locators(object):
    page_name = 'h2[class="SettingsSection_settings-section-header__uXJhj"]'
    Search_bar = 'input[placeholder="Search settings"]'
    your_account ="/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]"
    Twitter_blue = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]"
    Security_and_Account = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[3]"
    Privacy_and_safety = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[4]"
    notifications = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[5]"
    accessbility = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[6]"
    resources = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[7]"

    your_account_ident ="/html/body/div[1]/div/div/div[2]/div[2]/h2"
    Twitter_blue_ident = " "
    Security_and_Account_ident = " "
    Privacy_and_safety_ident = " "
    notifications_ident = " "
    accessbility_ident = " "
    resources_ident = " "

    search_result = " "

class Side_bar_Locators(object):
    Home = "/html/body/div[1]/div/div/div[1]/div[2]/a/div"
    Explore = "/html/body/div[1]/div/div/div[1]/div[3]/a/div"
    Notifications = "/html/body/div[1]/div/div/div[1]/div[4]/a/div"
    Messages = "/html/body/div[1]/div/div/div[1]/div[5]/a/div"
    bookmark = "/html/body/div[1]/div/div/div[1]/div[6]/a/div"
    lists = "/html/body/div[1]/div/div/div[1]/div[7]/a/div"
    profile = "/html/body/div[1]/div/div/div[1]/div[8]/a/div"
    more = "/html/body/div/div/div/div[1]/div[9]"
    tweet_box = "/html/body/div[1]/div/div/div[1]/div[10]/div"

    Settings_more = "/html/body/div[1]/div/div/div[1]/div[1]/div/div/div/ul/div[7]/a/div"
    topics = "/html/body/div[1]/div/div/div[1]/div[1]/div/div/div/ul/div[1]/a/div"

    Settings_identifier = "/html/body/div[1]/div/div/div[2]/div[1]/h2"  # header of page
    Home_ident = "/html/body/div[1]/div/div/div[2]/h2"

    tweet_box_itself = ""
    

sign_in = "/html/body/div/div/div[1]/div[1]/div/div[5]/a"
email_field = "/html/body/div/div/div/div/div/div[2]/div/form/div/div/input"
next_button = '/html/body/div/div/div/div/div/div[2]/div/div[3]/p'
pass_field = "/html/body/div[1]/div/div/div/div/div/div[2]/form[2]/div/div/input"
log_in_button = "/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/button"
