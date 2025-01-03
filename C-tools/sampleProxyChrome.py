from DrissionPage import Chromium
from flaskServer.config.chromiumOptions import initChromiumOptions
from flaskServer.utils.chrome import getChromiumOptions
from flaskServer.services.dto.proxy import getProxyByID
from flaskServer.services.dto.env import getChoiceEnvs
from flaskServer.services.dto.account import getAccountById

def initChrom(chrome,env,http_host,http_port,user,pw):
    # 设置代理
    chrome.new_tab(
        f"chrome-extension://mnloefcpaepkpmhaoipjkpikbnkmbnic/options.html?env={env}&user={user}&pass={pw}&http_host={http_host}&http_port={http_port}")
    chrome.new_tab("chrome-extension://mnloefcpaepkpmhaoipjkpikbnkmbnic/popup.html")
    chrome.new_tab(
        f"chrome-extension://mnloefcpaepkpmhaoipjkpikbnkmbnic/options.html?env={env}&user={user}&pass={pw}&http_host={http_host}&http_port={http_port}")

chrome = Chromium(addr_or_opts=getChromiumOptions(initChromiumOptions("custom_env", 30000, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36", None)))


for i,env in enumerate(getChoiceEnvs()):
    if i==1:
        proxy = getProxyByID(env.t_proxy_id)
        discord = getAccountById(env.discord_id)
        # initChrom(chrome, "custom_env", proxy.ip, proxy.port, proxy.user, proxy.pwd)

        # tab = chrome.new_tab(f"https://discord.com?discordtoken={discord.token}")
        # chrome.close_tabs(tabs_or_ids=tab, others=True)
        # tab.set.local_storage("token", f'"{discord.token}"')
        # tab = chrome.new_tab("https://discord.com/channels/@me")
        # chrome.close_tabs(tabs_or_ids=tab, others=True)

        tab = chrome.new_tab(f"https://x.com/home")
        chrome.close_tabs(tabs_or_ids=tab, others=True)
        tab.set.cookies(f'name=auth_token; value={"a9cb7b50043c5adad3e3111e86b31d7c1ecb0d53"};domain=.x.com;')
        tab = chrome.new_tab(f"https://x.com/home")
        chrome.close_tabs(tabs_or_ids=tab, others=True)





