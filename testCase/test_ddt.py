#!/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
from webDDT.pageOBJ.init import *
from webDDT.pageOBJ.loginPage import *
from ddt import *
from webDDT.untis import helper

# @ddt.ddt
# class loginDdt(init,login):
#     @ddt.data(('','',u'请您输入手机/邮箱/用户名'),('18291875606','',u'请您输入密码'),('18291875606','123456',u'请您输入验证码'))
#     @ddt.unpack
#     def test_all(self,name,pw,error):
#         self.login(name,pw)
#         self.assertEqual(self.getError,error)
#
# if __name__=='__main__':
#     unittest.main(verbosity=2)




@ddt
class loginDdt(init,login):
    @data(('','',u'请您输入手机/邮箱/用户名'),('18291875606','',u'请您输入密码'),('18291875606','123456',u'请您输入验证码'))
    @unpack
    def test_all(self,name,pw,error):
        self.login(name,pw)
        self.assertEqual(self.getError,error)

if __name__=='__main__':
    unittest.main(verbosity=2)


#ddt使用的数据放在列表中
@ddt
class loginDdt(init,login):
     @data(*helper.readlist())
     @unpack
     def test_all(self,name,pw,error):
         self.login(name,pw)
         self.assertEqual(self.getError,error)

if __name__=='__main__':
     unittest.main(verbosity=2)






