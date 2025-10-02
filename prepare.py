def generateLED(remainingMines):
    led = np.zeros((35,60,3), dtype=np.uint8);
    if remainingMines > 1000:
        remainingMines = 999
    digits = str(remainingMines)
    while len(digits) < 3:
        digits = '0' + digits;
    for i, num in enumerate(digits):
        texture = cv2.imread("images/led" + num + ".png", cv2.IMREAD_COLOR)
        x1 = i * 20
        x2 = (i+1)* 20
        led[0:35,x1:x2] = texture
        pass
    cv2.imwrite('led.png', led)