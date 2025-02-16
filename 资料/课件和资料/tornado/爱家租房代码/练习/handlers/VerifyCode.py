# coding:utf-8

from BaseHandler import BaseHandler
from utils.captcha import captcha
from constants import PIC_CODE_EXPIRES_SECONDS
import os
import logging

"""
获取验证码
生成验证码
返回验证码
"""

class PicCodeHandler(BaseHandler):
    """图片验证码"""
    def get(self):
        """获取图片验证码"""
        pre_code_id = self.get_argument("pre", "")
        cur_code_id = self.get_argument("cur")
        # 生成图片验证码
        name, text, pic = captcha.generate_captcha()
        try:
            if pre_code_id:
                self.redis.delete("pic_code_%s" % pre_code_id)
            # self.redis.setex(name, expries, value)
            self.redis.setex("pic_code_%s" % cur_code_id, PIC_CODE_EXPIRES_SECONDS, text)
        except Exception as e:
            logging.error(e)
            self.write("")
        else:
            self.set_header("Content-Type", "image/jpg")
            self.write(pic)



