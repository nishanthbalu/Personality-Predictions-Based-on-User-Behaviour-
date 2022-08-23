from django.shortcuts import render
from .models import user_login,user_post,data_set,label_master,user_details,category_master,user_pic,label_category_map,user_question
from django.db.models import Max
import os
from .topic_classification import TopicClassification
from project.settings import BASE_DIR
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'./myapp/index.html')

def about(request):
    return render(request,'./myapp/about.html')

def contact(request):
    return render(request,'./myapp/contact.html')

def admin_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd)

        if len(ul) == 1:
            request.session['user_id'] = ul[0].uname
            context = {'uname': request.session['user_id']}
            return render(request, 'myapp/admin_home.html',
                          context)
        else:
            return render(request, 'myapp/admin_login.html')
    else:
        return render(request, 'myapp/admin_login.html')

def admin_home(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_home.html',context)

def admin_settings(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_settings.html',context)

def admin_settings_404(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_settings_404.html',context)

def admin_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_id']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                return render(request, './myapp/admin_settings.html')
            else:
                return render(request, './myapp/admin_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/admin_changepassword.html')
    else:
        return render(request, './myapp/admin_changepassword.html')


def admin_category_master_add(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        cm = category_master(category_name=category_name)
        cm.save()
        return render(request, 'myapp/admin_category_master_add.html')

    else:
        return render(request, 'myapp/admin_category_master_add.html')

def admin_category_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = category_master.objects.get(id=int(id))
    nm.delete()

    nm_l = category_master.objects.all()
    context ={'category_list':nm_l}
    return render(request,'myapp/admin_category_master_view.html',context)

def admin_category_master_view(request):
    nm_l = category_master.objects.all()
    context ={'category_list':nm_l}
    return render(request,'myapp/admin_category_master_view.html',context)

def admin_category_map_add(request):
    if request.method == 'POST':
        label_id = int(request.POST.get('label_id'))
        category_id = int(request.POST.get('category_id'))
        cm = label_category_map(category_id=category_id,label_id=label_id)
        cm.save()
        cm_l = category_master.objects.all()
        lm_l = label_master.objects.all()

        context = {'msg':'Record Added','category_list': cm_l,'label_list':lm_l}
        return render(request, 'myapp/admin_category_map_add.html',context)

    else:
        cm_l = category_master.objects.all()
        lm_l = label_master.objects.all()

        context = {'category_list': cm_l,'label_list':lm_l}
        return render(request, 'myapp/admin_category_map_add.html',context)

def admin_category_map_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = label_category_map.objects.get(id=int(id))
    nm.delete()

    nm_l = label_category_map.objects.all()

    lm_l = label_master.objects.all()
    lmd = {}
    for nm in lm_l:
        lmd[nm.id] = nm.label
    cm_l = category_master.objects.all()
    cmd = {}
    for nm in cm_l:
        cmd[nm.id] = nm.category_name
    context ={'msg':'Record Removed','map_list':nm_l,'label_list':lmd,'category_list':cmd}
    return render(request,'myapp/admin_category_map_view.html',context)

def admin_category_map_view(request):
    nm_l = label_category_map.objects.all()

    lm_l = label_master.objects.all()
    lmd = {}
    for nm in lm_l:
        lmd[nm.id] = nm.label
    cm_l = category_master.objects.all()
    cmd = {}
    for nm in cm_l:
        cmd[nm.id] = nm.category_name
    context = {'msg': 'Record Removed', 'map_list': nm_l, 'label_list': lmd, 'category_list': cmd}
    return render(request, 'myapp/admin_category_map_view.html', context)


def admin_label_master_add(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        cm = label_master(label=label)
        cm.save()
        return render(request, 'myapp/admin_label_master_add.html')

    else:
        return render(request, 'myapp/admin_label_master_add.html')

def admin_label_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = label_master.objects.get(id=int(id))
    nm.delete()

    nm_l = label_master.objects.all()
    context ={'label_list':nm_l}
    return render(request,'myapp/admin_label_master_view.html',context)

def admin_label_master_view(request):
    nm_l = label_master.objects.all()
    context ={'label_list':nm_l}
    return render(request,'myapp/admin_label_master_view.html',context)

def admin_user_details_view(request):

    ul_l = user_login.objects.filter(utype='user')
    nm_l = list()
    for ul in ul_l:
        nm_l.append(user_details.objects.get(user_id=ul.id))

    context ={'user_list':nm_l}
    return render(request,'myapp/admin_user_details_view.html',context)

def admin_doctor_details_view(request):

    ul_l = user_login.objects.filter(utype='doctor')
    nm_l = list()
    for ul in ul_l:
        nm_l.append(user_details.objects.get(user_id=ul.id))

    context ={'user_list':nm_l}
    return render(request,'myapp/admin_doctor_details_view.html',context)


from collections import Counter
def admin_user_posts_analyse(request):
    user_id = int(request.GET.get('id'))
    #print("id="+id)

    up_l = user_post.objects.filter(user_id=user_id)
    p_l_map = list()
    percentages = 0
    ##################################
    obj = TopicClassification()

    data_file_path = os.path.join(BASE_DIR, 'data/data_set.csv')
    data_file_label_path = os.path.join(BASE_DIR, 'data/data_set_label.dat')
    tfid_file_path = os.path.join(BASE_DIR, 'data/data_set_tfid.dat')
    model_file_path = os.path.join(BASE_DIR, 'data/data_set_svm.model')
    for up in up_l:
        model = obj.load_data(model_file_path)
        Tfidf_vect = obj.load_data(tfid_file_path)
        result = obj.input_text_processing(up.msg)
        p = obj.get_prediction(model, result, Tfidf_vect)
        label = obj.load_data(data_file_label_path)
        label = sorted(label)
        print(f'result = {label[p[0]]}')
        final_label = label[p[0]]
        obj_label = label_master.objects.get(label=final_label)
        obj_map = label_category_map.objects.get(label_id=obj_label.id)
        obj_category = category_master.objects.get(id=obj_map.category_id)
        p_l_map.append(obj_category.category_name)


        count = Counter(p_l_map).items()

        percentages = {x: int(float(y) / len(p_l_map) * 100) for x, y in count}

        #for name, pct in percentages.iteritems():
        #    print('%s - %s%s' % (name, pct, '%'))
        print(percentages)
        for i in count:
            print(i)

    ####################################
    print(p_l_map)
    nm_l = user_details.objects.all()
    context = {'msg': percentages}
    return render(request, 'myapp/admin_user_analyse_result.html', context)


def admin_data_set_add(request):
    if request.method == 'POST':
        label_id=int(request.POST.get('label_id'))
        fpath=request.POST.get('fpath')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status='ok'

        cm = data_set(label_id=label_id,fpath=fpath,dt=dt,tm=tm,status=status)
        cm.save()

        ##########training model############
        data_file_path = os.path.join(BASE_DIR, 'data/data_set.csv')
        #os.remove(data_file_path)

        obj_list = data_set.objects.all()
        if len(obj_list) >3:
            f = open(data_file_path, "w")
            f.write('text,label')
            f.write("\n")
            for obj in obj_list:
                lb = label_master.objects.get(id=obj.label_id)
                f.write(f'{obj.fpath},{lb.label}')
                f.write("\n")
            f.close()
            data_file_path = os.path.join(BASE_DIR, 'data/data_set.csv')
            data_file_label_path = os.path.join(BASE_DIR, 'data/data_set_label.dat')
            tfid_file_path = os.path.join(BASE_DIR, 'data/data_set_tfid.dat')
            model_file_path = os.path.join(BASE_DIR, 'data/data_set_svm.model')

            obj = TopicClassification()
            txt_result = obj.text_processing(data_file_path,data_file_label_path)
            obj.train_model(txt_result,tfid_file_path,model_file_path,'svm')
            ################
        nm_l = label_master.objects.all()
        context = {'label_list': nm_l,'msg':'Record Added'}
        return render(request, 'myapp/admin_data_set_add.html',context)

    else:
        nm_l = label_master.objects.all()
        for nm in nm_l:
            print(nm.id)
        context = {'label_list': nm_l, 'msg': ''}
        return render(request, 'myapp/admin_data_set_add.html',context)

def admin_data_set_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = data_set.objects.get(id=int(id))
    nm.delete()

    nm_l = data_set.objects.all()
    cmd = {}
    for nm in nm_l:
        lb = label_master.objects.get(id=nm.label_id)
        cmd[nm.label_id] = lb.label

    context ={'data_list':nm_l,'label_list':cmd,'msg':'Record Deleted'}
    return render(request,'myapp/admin_data_set_view.html',context)

def admin_data_set_view(request):
    nm_l = data_set.objects.all()
    cmd = {}
    for nm in nm_l:
        lb = label_master.objects.get(id=nm.label_id)
        cmd[nm.label_id] = lb.label

    context = {'data_list': nm_l, 'label_list': cmd, 'msg': ''}
    return render(request, 'myapp/admin_data_set_view.html', context)





########USER#############
def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd,utype='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/user_home.html',context)
        else:
            context={'msg':'Invalid username or password'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname=email
        status = "new"

        ul = user_login(uname=uname, password=password, utype='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, addr=addr, pin=pin, contact=contact,
                               status=status,email=email )
        ud.save()

        print(user_id)

        return render(request, 'myapp/user_login.html')

    else:
        return render(request, 'myapp/user_details_add.html')
def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                return render(request, './myapp/user_settings.html')
            else:
                return render(request, './myapp/user_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/user_changepassword.html')
    else:
        return render(request, './myapp/user_changepassword.html')

def user_settings(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_settings.html',context)
import os
def user_posts_add(request):
    if request.method == 'POST':

        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'safe'
        msg = request.POST.get('msg')
        user_id=int(request.session['user_id'])
        km = user_post( user_id=user_id, msg=msg, dt=dt, tm=tm, status=status)
        km.save()
        context={'msg':'Post added'}
        return render(request, 'myapp/user_posts_add.html',context)
    else:
        return render(request, 'myapp/user_posts_add.html')

def user_posts_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = user_post.objects.get(id=int(id))
    nm.delete()
    user_id = int(request.session['user_id'])
    nm_l = user_post.objects.filter(user_id=user_id)
    context ={'posts_list':nm_l,'msg':'Post deleted'}
    return render(request,'myapp/user_posts_view.html',context)

def user_posts_view(request):
    user_id = int(request.session['user_id'])
    nm_l = user_post.objects.filter(user_id=user_id)
    context = {'posts_list': nm_l}
    return render(request, 'myapp/user_posts_view.html', context)

from django.core.files.storage import FileSystemStorage
def user_pic_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pic_path = fs.save(uploaded_file.name, uploaded_file)
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'safe'

        user_id=int(request.session['user_id'])
        km = user_pic( user_id=user_id, pic_path=pic_path, dt=dt, tm=tm, status=status)
        km.save()
        context={'msg':'Picture added'}
        return render(request, 'myapp/user_pic_add.html',context)
    else:
        return render(request, 'myapp/user_pic_add.html')

def user_pic_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = user_pic.objects.get(id=int(id))
    nm.delete()
    user_id = int(request.session['user_id'])
    nm_l = user_pic.objects.filter(user_id=user_id)
    context ={'pic_list':nm_l,'msg':'Pic deleted'}
    return render(request,'myapp/user_pic_view.html',context)

def user_pic_view(request):
    user_id = int(request.session['user_id'])
    nm_l = user_pic.objects.filter(user_id=user_id)
    context = {'pic_list': nm_l}
    return render(request, 'myapp/user_pic_view.html', context)


def user_question_add(request):
    if request.method == 'POST':

        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        msg = request.POST.get('msg')
        user_id=int(request.session['user_id'])
        doctor_id = 0
        reply = 'reply'
        rdt = 'date'
        rtm = 'time'

        km = user_question(user_id=user_id, msg=msg, dt=dt, tm=tm, status=status,doctor_id=doctor_id,reply=reply,rdt=rdt,rtm=rtm)
        km.save()
        context={'msg':'Question added'}
        return render(request, 'myapp/user_question_add.html',context)
    else:
        return render(request, 'myapp/user_question_add.html')

def user_question_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = user_question.objects.get(id=int(id))
    nm.delete()
    user_id = int(request.session['user_id'])
    nm_l = user_question.objects.filter(user_id=user_id)

    lm_l = user_details.objects.filter(utype='doctor')
    lmd = {}
    for nm in lm_l:
        lmd[nm.user_id] = f'{nm.fname} {nm.lname}'


    context ={'question_list':nm_l,'doctor_list':lmd,'msg':'Question deleted'}
    return render(request,'myapp/user_question_view.html',context)

def user_question_view(request):
    user_id = int(request.session['user_id'])
    nm_l = user_question.objects.filter(user_id=user_id)

    lm_l = user_login.objects.filter(utype='doctor')
    lmd = {}
    for nm in lm_l:
        ud = user_details.objects.get(user_id=nm.id)
        lmd[nm.id] = f'{ud.fname} {ud.lname}'

    context = {'question_list': nm_l, 'doctor_list': lmd, 'msg': ''}
    return render(request, 'myapp/user_question_view.html', context)


########doctor#############
def doctor_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd,utype='doctor')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/doctor_home.html',context)
        else:
            context={'msg':'Invalid username or password'}
            return render(request, 'myapp/doctor_login.html',context)
    else:
        return render(request, 'myapp/doctor_login.html')

def doctor_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/doctor_home.html',context)

def doctor_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname=email
        status = "new"

        ul = user_login(uname=uname, password=password, utype='doctor')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, addr=addr, pin=pin, contact=contact,
                               status=status,email=email )
        ud.save()

        print(user_id)
        context={'msg':'Doctor registered'}
        return render(request, 'myapp/doctor_login.html',context)

    else:
        return render(request, 'myapp/doctor_details_add.html')

def doctor_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                return render(request, './myapp/doctor_settings.html')
            else:
                return render(request, './myapp/doctor_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/doctor_changepassword.html')
    else:
        return render(request, './myapp/doctor_changepassword.html')

def doctor_settings(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/doctor_settings.html',context)

def doctor_question_view(request):
    user_id = int(request.session['user_id'])
    nm_l = user_question.objects.filter(doctor_id=0)

    lm_l = user_login.objects.filter(utype='user')
    lmd = {}
    for nm in lm_l:
        ud = user_details.objects.get(user_id=nm.id)
        lmd[nm.id] = f'{ud.fname} {ud.lname}'

    context = {'question_list': nm_l, 'user_list': lmd, 'msg': ''}
    return render(request, 'myapp/doctor_question_view.html', context)

def doctor_reply_view(request):
    user_id = int(request.session['user_id'])
    nm_l = user_question.objects.filter(doctor_id=user_id)

    lm_l = user_login.objects.filter(utype='user')
    lmd = {}
    for nm in lm_l:
        ud = user_details.objects.get(user_id=nm.id)
        lmd[nm.id] = f'{ud.fname} {ud.lname}'

    context = {'question_list': nm_l, 'user_list': lmd, 'msg': ''}
    return render(request, 'myapp/doctor_reply_view.html', context)
def doctor_reply_add(request):
    if request.method == 'POST':
        msg_id = request.POST.get('msg_id')
        print(msg_id)
        obj = user_question.objects.get(id=int(msg_id))

        obj.rdt = datetime.today().strftime('%Y-%m-%d')
        obj.rtm = datetime.today().strftime('%H:%M:%S')
        obj.status = 'answered'
        obj.reply = request.POST.get('msg')
        obj.doctor_id = int(request.session['user_id'])

        obj.save()

        context={'msg':'Answer added'}
        return render(request, 'myapp/doctor_question_view.html',context)
    else:
        msg_id = request.GET.get('id')
        context={'msg_id':msg_id}
        return render(request, 'myapp/doctor_reply_add.html',context)
