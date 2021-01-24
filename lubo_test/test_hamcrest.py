from hamcrest import *

def test_hamrest():
   assert_that(10, equal_to(10), '这是一个异常提示')
   assert_that(8, close_to(10,2))
