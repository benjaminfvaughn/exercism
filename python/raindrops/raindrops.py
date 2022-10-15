def convert(number):
    raindrops=''
    factor = False
    if number % 3==0:
        raindrops = 'Pling'
        factor = True
    if number % 5==0:
        raindrops = raindrops+'Plang'
        factor = True
    if number % 7==0:
        raindrops = raindrops+'Plong'
        factor = True
    if not factor:
        return str(number)
    else:
        return raindrops
