from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from .models import teacher,student,equipment,quanxian,yuyue
import json
from django.shortcuts import render,redirect
from .datecal import dateRange
import datetime
# Create your views here.
from .models import student
from django.db.models import Max,F,Q
from django.contrib.auth import authenticate, login,get_user
from django.db.models import F, FloatField, Sum
def stusqupdateepi(request):

    jsonstring = json.loads(request.body.decode())
    stuid = jsonstring["stuidstr"]
    quanxians=quanxian.objects.filter(qsid__sid=stuid).values_list("qeid__eid")

    values=[]
    for item in quanxians:
        print(item[0])
        values.append(item[0])

    return JsonResponse({"data": values})



def chongxinfenpei1(request):
    jsonstring = json.loads(request.body.decode())

    stuid = jsonstring["stuid"]
    print("stuid:",stuid)
    quanxian.objects.filter(qsid__sid=stuid).delete()

    values=jsonstring["values"]
    print("values:",values)
    herestudent=student.objects.get(sid=stuid)
    for value in values:
        hereequipment=equipment.objects.get(eid=value)
        newquanxian=quanxian()
        newquanxian.qsid=herestudent
        newquanxian.qeid=hereequipment
        newquanxian.save()

    return JsonResponse({"data": "成功"})


def chongxinfenpei2(request):
    jsonstring = json.loads(request.body.decode())

    stus = jsonstring["stus"]
    print("stuid:", stus)
    values = jsonstring["values"]
    print("values:", values)
    for stupk in stus:

        cc=quanxian.objects.filter(qsid__spk=stupk).delete()
        # cc=quanxian.objects.filter(qsid__sid=stupk)
        print("cc:",cc)


        herestudent = student.objects.get(spk=stupk)
        print("heresstudent:",herestudent)
        for value in values:
            print("value:",value)
            hereequipment = equipment.objects.get(eid=value)
            print("hereequipment:",hereequipment)
            newquanxian = quanxian()
            newquanxian.qsid = herestudent
            newquanxian.qeid = hereequipment
            print("newquanxian:",newquanxian)
            newquanxian.save()
            print("222")

    return JsonResponse({"data": "成功"})

def tianjia1(request):
    jsonstring = json.loads(request.body.decode())

    stuid = jsonstring["stuid"]

    eids=quanxian.objects.filter(qsid__sid=stuid).values_list("qeid__eid")

    neweids=[]
    for ei in eids:
        neweids.append(ei[0])


    values = jsonstring["values"]
    values=[int(x) for x in values]
    newvalues=[]
    for val in values:
        if(val not in neweids):
            newvalues.append(val)

    herestudent = student.objects.get(sid=stuid)
    for value in newvalues:
        hereequipment = equipment.objects.get(eid=value)
        newquanxian = quanxian()
        newquanxian.qsid = herestudent
        newquanxian.qeid = hereequipment
        newquanxian.save()

    return JsonResponse({"data": "成功"})

def tianjia2(request):
    jsonstring = json.loads(request.body.decode())
    stus= jsonstring["stus"]
    stus=[int(y) for y in stus]
    print("stus:",stus)
    for stupk in stus:
        eids = quanxian.objects.filter(qsid__spk=stupk).values_list("qeid__eid")
        neweids = []
        for ei in eids:
            neweids.append(ei[0])
        values = jsonstring["values"]
        values = [int(x) for x in values]
        newvalues = []
        for val in values:
            if (val not in neweids):
                newvalues.append(val)
        herestudent = student.objects.get(spk=stupk)
        for value in newvalues:
            hereequipment = equipment.objects.get(eid=value)
            newquanxian = quanxian()
            newquanxian.qsid = herestudent
            newquanxian.qeid = hereequipment
            newquanxian.save()
    return JsonResponse({"data": "成功"})




def shanchu1(request):
    print("shanchu1")
    jsonstring = json.loads(request.body.decode())

    stuid = jsonstring["stuid"]

    eids = quanxian.objects.filter(qsid__sid=stuid).values_list("qeid__eid")

    neweids = []
    for ei in eids:
        neweids.append(ei[0])

    values = jsonstring["values"]
    values = [int(x) for x in values]
    newvalues = []
    for val in values:
        if (val  in neweids):
            newvalues.append(val)

    herestudent = student.objects.get(sid=stuid)
    print("newvalues:",newvalues)
    for value in newvalues:
        hereequipment = equipment.objects.get(eid=value)
        newquanxian = quanxian()
        newquanxian.qsid = herestudent
        newquanxian.qeid = hereequipment
        quanxian.objects.filter(qeid=hereequipment,qsid=herestudent).delete()

    return JsonResponse({"data": "成功"})
def shanchu2(request):
    jsonstring = json.loads(request.body.decode())
    stus = jsonstring["stus"]
    stus = [int(y) for y in stus]
    print("stus:", stus)
    for stupk in stus:
        eids = quanxian.objects.filter(qsid__spk=stupk).values_list("qeid__eid")
        neweids = []
        for ei in eids:
            neweids.append(ei[0])
        values = jsonstring["values"]
        values = [int(x) for x in values]
        newvalues = []
        for val in values:
            if (val  in neweids):
                newvalues.append(val)
        herestudent = student.objects.get(spk=stupk)
        for value in newvalues:
            hereequipment = equipment.objects.get(eid=value)

            quanxian.objects.filter(qeid=hereequipment,qsid=herestudent).delete()

    return JsonResponse({"data": "成功"})


def studentshenqing(request):
    queryxuehao = request.GET.get('xuehao', default='')
    queryname = request.GET.get('name', default='')
    queryteacher = request.GET.get('teacher', default='')
    startdate = request.GET.get('timestart', default='')
    enddate = request.GET.get('timeend', default='')
    print('queryxuehao:', queryxuehao)
    print('queryname:', queryname)
    print('queryteacher:', queryteacher)
    print('startdate:', startdate)
    print('enddate:', enddate)
    if (startdate == ""):

        startquery = ""
        startTime = datetime.datetime.strptime('2019/01/01', '%Y/%m/%d').date()
    else:
        startquery = startdate
        startTime = datetime.datetime.strptime(startdate, '%Y/%m/%d').date()

    if (enddate == ""):
        endquery = ""
        endTime = datetime.date.today()
    else:
        endquery = enddate
        endTime = datetime.datetime.strptime(enddate, '%Y/%m/%d').date()

    studentall = student.objects.filter(Q(istongguo=True),Q(sname__icontains=queryname),
                                      Q(sid__icontains=queryxuehao), Q(steacher__tname__icontains=queryteacher),
                                      Q(time__gte=startTime),
                                      Q(time__lte=endTime))




    students=[]
    for student1 in studentall:
        spk=student1.spk
        sname=student1.sname
        sid=student1.sid
        teachname=student1.steacher
        time=student1.time
        sss={"spk":spk,"sname":sname,"sid":sid,"teachername":teachname,"time":time}
        students.append(sss)

    print("student1:",students)
    equipments=equipment.objects.all()
    equip = []
    i=0
    for i in range(len(equipments) // 3):
        sss = equipments[i * 3:i * 3 + 3]
        equip.append(sss)
    if (len(equipments) % 3):
        equip.append(equipments[i*3+3:])


    return render(request,"studentshenqing.html",{"students":students,"equipments":equip})



def xiaowaitongguo(request):

    jsonstring = json.loads(request.body.decode())
    stuid = jsonstring["stuid"]
    print("xiaowaitongguo:",stuid)
    studentpk=student.objects.filter(sid=stuid)
    print("studentpk:",studentpk[0])
    print(type(studentpk))
    print("#################################")


    print("end:", studentpk[0].isshenhe)



    quanxianlist=quanxian.objects.filter(qsid=studentpk[0])
    print("quanxianlist:",quanxianlist)
    quanxianlist.delete()
    print("shanchuchenggong")


    equips=equipment.objects.all()
    for equip in equips:
        newone = quanxian(qsid=studentpk[0], qeid=equip)
        newone.save()




    studente=student.objects.get(sid=stuid)
    studente.isshenhe = 1
    studente.istongguo=1
    studente.save()
    return JsonResponse({"data": "mydata"})


def foradmin2(request):
    if not request.user.is_authenticated():
    # if str(user) == "AnonymousUser":
        return HttpResponseRedirect('/admin/login/')
    else:
        # newstudents=student.objects.filter(Q(isshenhe=False),Q(isstudent=True))

        # newzuwairenyuan=student.objects.filter(Q(isshenhe=False),Q(isstudent=False))
        # number2=len(newzuwairenyuan)
        # print("number:",number1)

        newstudents = student.objects.filter( Q(isshenhe=False))
        number1 = len(newstudents)
        equipments = equipment.objects.all()
        students =[]
        if(len(newstudents)<=3):
            students=newstudents
        else:
            students=newstudents[:3]

        return render(request,'foradmin2.html',{"number1":number1,'students':students,'equipments':equipments})



def shebeiform(request):


        queryname = request.GET.get('name', default='')
        startdate = request.GET.get('timestart', default='')
        enddate = request.GET.get('timeend', default='')
        if (startdate == ""):
            startquery = ""
            startTime = datetime.datetime.strptime('2019/01/01', '%Y/%m/%d').date()
        else:
            startquery = startdate
            startTime = datetime.datetime.strptime(startdate, '%Y/%m/%d').date()

        if (enddate == ""):
            endquery = ""
            endTime = datetime.date.today()
        else:
            endquery = enddate
            endTime = datetime.datetime.strptime(enddate, '%Y/%m/%d').date()

        shebei1 = yuyue.objects.filter(Q(yeid__ename__icontains=queryname), Q(ydate__gte=startTime),
                                       Q(ydate__lte=endTime),Q(isquxiao=False))
        shebeis = shebei1.values_list("yeid__eid", "yeid__ename","ysid__sname","qiandaoshijian","ydate","ytimestart","shichang","isqiandao","yuyuebeizhu","shiyanfankui").order_by('yeid__eid','ydate',"ytimestart")

        result = []
        for index ,row in enumerate(shebeis):
            eid = index+1
            ename = row[1]
            sname=row[2]
            qiandaoshijian=row[3]
            ydate=row[4]
            ystarttime=row[5]
            shichang=row[6]
            isqiandao=row[7]
            yuyuebeizhu=row[8]
            shiyanfankui=row[9]
            result.append({"eid": eid, "ename": ename, "sname": sname,"ydate":ydate,"ystarttime":ystarttime,"shichang":shichang,"isqiandao":isqiandao,"yuyuebeizhu":yuyuebeizhu,"shiyanfankui":shiyanfankui})

        return render(request, 'shebeiform.html',
                      {"startquery": startquery, "endquery": endquery, "queryname": queryname, "starttime": startTime,
                       "endtime": endTime, "shebeis": result})
