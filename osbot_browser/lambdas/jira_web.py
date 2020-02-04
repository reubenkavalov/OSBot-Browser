from gw_bot.helpers.Lambda_Helpers import slack_message
from osbot_browser.browser.Browser_Commands import load_dependencies


def run(event, context):
    load_dependencies('syncer,requests,pyppeteer')
    issue_id = event.get('issue_id')
    channel  = event.get('channel')
    team_id  = event.get('team_id')
    width    = event.get('width')
    height   = event.get('height')

    try:
        from osbot_browser.browser.sites.Web_Jira import Web_Jira
        wait     = event.get('wait',2)
        web_jira = Web_Jira(headless=False).setup()

        from time import sleep
        #sleep(2)                        # still needs this
        #web_jira.login()
        #web_jira.issue(issue_id)

        #
        #sleep(2)
        #return web_jira.page.url()
        #return web_jira.screenshot()
        slack_message(':one: Logging in', [] ,channel)
        web_jira.login()  #web_jira.fix_set_list_view()

        slack_message(f':two: opening issue `{issue_id}` in headless chrome', [], channel)
        web_jira.issue(issue_id)
        #return web_jira.screenshot()

        #sleep(wait)

        web_jira.fix_issue_remove_ui_elements()
        if width is None:
            width = 1200
        if height is None:
            height = 300

        #slack_message(':three: taking screenshot', [], channel)
        png_data =  web_jira.screenshot(width, height)

        if channel:
            from osbot_browser.browser.Browser_Lamdba_Helper import Browser_Lamdba_Helper
            title = "Issue: {0}".format(issue_id)
            slack_message(f':three: sending screenshot to slack image with size {len(png_data)}', [], channel)
            Browser_Lamdba_Helper().send_png_data_to_slack(team_id, channel, title, png_data)
            return "sent png to slack"

    except Exception as error:
        message = f'Error in jira_web lambda: {error}'
        slack_message(message,[],channel)
        return message
    return png_data