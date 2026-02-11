class Gun:
    def __init__(self, shoots='pif'):
        self.shoots = shoots

    def shoot(self):
        print(self.shoots)
        if self.shoots == 'pif':
            self.shoots = 'paf'
        elif self.shoots == 'paf':
            self.shoots = 'pif'

gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()