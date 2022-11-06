
def computed_property(*args):

    class computed_property_prospector(object):
        def __init__(self, fget=None, fset=None, fdel=None, doc=None, dependencies=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            if doc is None and fget is not None:
                doc = fget.__doc__
            self.dependencies = dependencies
            self.cached = dict()
            self.__doc__ = doc

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError("unreadable attribute")
            dependencies = None
            if hasattr(objtype, self.fget.__name__):
                if hasattr(getattr(objtype, self.fget.__name__), 'dependencies'):
                    dependencies = getattr(getattr(objtype, self.fget.__name__), 'dependencies')
                if dependencies is None:
                    return self.fget(obj)
                else:
                    allowed_dependencies = tuple([x for x in dependencies if hasattr(obj, x)])
                    key_cache = tuple([getattr(obj, x) for x in allowed_dependencies])
                    if self.cached.get(key_cache):
                        result = self.cached.get(key_cache)
                    else:
                        result = self.fget(obj)
                        self.cached[key_cache] = result
                    return result
            else:
                return self.fget(obj)

        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError("can't set attribute")
            self.fset(obj, value)

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError("can't delete attribute")
            self.fdel(obj)

        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel, self.__doc__, self.dependencies)

        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel, self.__doc__, self.dependencies)

        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel, self.__doc__, self.dependencies)

    return computed_property_prospector
