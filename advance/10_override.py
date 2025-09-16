class Car:
    def start(self):
        print('시동이 걸린다.')

    def run(self):
        print('차가 시속 50km 로 달린다.')

    def stop(self):
        print('차가 멈춘다.')

class MyCar(Car):

    turbo = False

    def run(self): #부모와 같은 매서드를 사용하면 override로 인식된다.
        if self.turbo == True:
            print('차가 시속 200km 로 달린다.')
        else:
            super().run()


mc = MyCar()
mc.start()

mc.run()   ##부모클래스에서는 50km로 나와야하는데 자식클래스에서 똑같은 매서드를 사용해서 override가 구현됨.
turbo = True
mc.run()

mc.stop()
