#!/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
from webDDT.webUI.pageOBJ.init import *
from webDDT.webUI.pageOBJ.loginPage import *
from ddt import *
from webDDT.untis import helper

@ddt
class loginDdt(init,login):
    @data(('','',u'请您输入手机/邮箱/用户名'),('18291875606','',u'请您输入密码'),('18291875606','123456',u'请您输入验证码'))
    @unpack
    def test_all(self,name,pw,error):
        self.login(name,pw)
        self.assertEqual(self.getError,error)








