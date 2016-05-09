class baseObject(object):
    # 给出模板对象
    def __init__(self, *args, **kargs):
        pass
    
    def __gt__(self, obj):
        raise ValueError("You must rewrite this abstract method: __gt__")
        
class mObject(baseObject):
    # 一个简单的例子
    def __init__(self, value=None):
        self.value = value
        
    def __eq__(self, obj):
        return self.value == obj.value
    
    def __repr__(self):
        return "{%s}" % self.value