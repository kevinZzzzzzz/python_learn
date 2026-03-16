class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

clock_1 = Clock()
clock_1.id = '003032'
clock_1.price = 10.29
print(f"闹钟ID: {clock_1.id},价格：{clock_1.price}")
clock_1.ring()


