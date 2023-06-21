



def pass_ball(n):

    if n == 0 :
        return 0

    if n == 1:
        return 1

    return  pass_ball(n-1) + pass_ball(n-2)



def angleclock( hour, minute):
    h = ( hour%12 * 30) + ( minute/60 + 30)
    m = minute * 6
    #angle = abs(m-h)

    angle = 0

    if (m-h) < 0:

        angle = 360 - abs(m-h)

    else :
        angle = m-h



    # if angle > 180 :
    #     angle = 360.0 - angle

    return angle

if __name__ == '__main__':
    #print(pass_ball(4))
    print(angleclock(3,0))

