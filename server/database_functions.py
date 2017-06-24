def intersection_number():
    no = Intersection.objects.count()
    if no == None:
        return str(1)
    else:
        return str(no + 1)


def trafficlights_number():
    no = TrafficLight.objects.count()
    if no == None:
        return str(1)
    else:
        return str(no + 1)


def centralnode_number():
    no = CentralNode.objects.count()
    if no == None:
        return str(1)
    else:
        return str(no + 1)