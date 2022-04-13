import json

from src.captcha import deathbycaptcha
from src.variables import dbc_percent, dbc_token, dbc_password, dbc_username
from src.util.logger import log


def solve_recaptcha(key, url, action, current=1, max_exec=1):
    try:
        Captcha_dict = {
            'proxy': '',
            'proxytype': '',
            'googlekey': key,
            "pageurl": url,
            'action': action,
            'min_score': dbc_percent}

        json_Captcha = json.dumps(Captcha_dict)
        client = deathbycaptcha.HttpClient(dbc_username, dbc_password, dbc_token)

        balance = client.get_balance()
        log(f"DBC - balance: {balance}")
        # Put your CAPTCHA type and Json payload here:
        captcha = client.decode(type=4, token_params=json_Captcha)
        if captcha:
            # The CAPTCHA was solved; captcha["captcha"] item holds its
            # numeric ID, and captcha["text"] item its list of "coordinates".
            log("CAPTCHA %s solved: %s" % (captcha["captcha"], captcha["text"]))
            if '':  # check if the CAPTCHA was incorrectly solved
                client.report(captcha["captcha"])

        token_access = captcha["text"]
        return token_access
    except Exception as ex:
        log('### --- {} --- ###'.format(ex))
        if current < max_exec:
            log(f"Captcha: Realizar nova tentativa, atual {current} - máxima: {max_exec}")
            return quebra_captcha(key, url, action, current + 1, max_exec)

        return None


def solve_image_captcha(imagem, timeout):
    client = deathbycaptcha.HttpClient(dbc_username, dbc_password, dbc_token)
    captcha = client.decode(imagem, timeout)
    if captcha['is_correct'] == True:
        texto_captcha = captcha['text']
        return texto_captcha
    return None
