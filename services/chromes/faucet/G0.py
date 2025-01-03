import random

from loguru import logger

from flaskServer.config.connect import app
from flaskServer.services.dto.env import getChoiceEnvs
from flaskServer.services.dto.wallet import getWalletByID
from flaskServer.mode.wallet import Wallet
from flaskServer.services.chromes.login import NoAccountChrome
from flaskServer.services.chromes.worker import submit

# 处理页面任务
def worker(env):
    chrome = None
    try:
        chrome = NoAccountChrome(env)
        tab = chrome.new_tab(url="https://faucet.0g.ai")
        okx = getWalletByID(env.okx_id)
        tab.ele("#address").input(okx.address)
        tab.ele("@type=submit").wait.enabled(timeout=200)
        tab.ele("@type=submit").click()
        h3 = tab.ele("@id=modal-title").text
        m2 = tab.ele("@class=mt-2").text
        if "Successful" in h3 or "Please" in m2:
            logger.info(f"{env.name}环境领取成功")
        chrome.wait(3,4)
    except Exception as e:
        logger.error(f"{env.name}: {e}")
    finally:
        if chrome:
            chrome.quit()

# 任务调度
def toDo():
    envs = getChoiceEnvs()
    submit(worker,envs)


if __name__ == '__main__':
    # 初始化环境
    # toDo2()
    # 0G任务领取
    toDo()


