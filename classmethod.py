class bird:
    wings=2
    @classmethod
    def print(cls,name):
        print('{} is having {} wings.'.format(name,cls.wings))
bird.print('sparrow')
bird.print('dove')