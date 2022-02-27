import os
import time

if __name__ == '__main__':
    print "***********env is loading now *********"
    os.system("chmod 777 main.py")
    os.system("chmod 777 *.tar.gz")

    os.system("for i in $(ls *.tar.gz);do tar xvf $i;done")
    time.sleep(3)
    os.chdir("repo")

    os.system("rpm -ivh --replacefiles libgpg-error-devel-1.12-3.el7.x86_64.rpm libgcrypt-devel-1.5.3-14.el7.x86_64.rpm")
    time.sleep(1)
    os.system("rpm -ivh --replacefiles zlib-1.2.7-19.el7_9.x86_64.rpm zlib-devel-1.2.7-19.el7_9.x86_64.rpm xz-devel-5.2.2-1.el7.x86_64.rpm")
    time.sleep(1)
    os.system("rpm -ivh --replacefiles libxml2-2.9.1-6.el7_9.6.x86_64.rpm libxml2-devel-2.9.1-6.el7_9.6.x86_64.rpm libxml2-python-2.9.1-6.el7_9.6.x86_64.rpm")
    time.sleep(1)
    os.system("rpm -ivh --replacefiles libxslt-1.1.28-6.el7.x86_64.rpm libxslt-devel-1.1.28-6.el7.x86_64.rpm")
    time.sleep(1)
    os.system("rpm -ivh --replacefiles python2-rpm-macros-3-34.el7.noarch.rpm python-libs-2.7.5-90.el7.x86_64.rpm")
    time.sleep(1)
    os.system("rpm -ivh --replacefiles python-srpm-macros-3-34.el7.noarch.rpm python-rpm-macros-3-34.el7.noarch.rpm python-2.7.5-90.el7.x86_64.rpm python-devel-2.7.5-90.el7.x86_64.rpm --nodeps --force")
    time.sleep(5)
    os.chdir("..")
    os.chdir("pycrypto-2.6")
    os.system("python setup.py install")
    time.sleep(1)

    os.chdir("..")
    os.chdir("soaplib-2.0.0-beta2")
    os.system("python setup.py install")
    time.sleep(5)

    os.chdir("..")
    os.chdir("lxml-3.2.1")
    os.system("python setup.py install")
    time.sleep(10)

    os.chdir("..")
    os.chdir("PyJWT-1.5.3")
    os.system("python setup.py install")
    time.sleep(1)

    os.chdir("..")
    os.system("pip install funcsigs-1.0.2-py2.py3-none-any.whl")
    os.system("pip install futures-3.3.0-py2-none-any.whl")
    os.system("pip install tzlocal-2.1-py2.py3-none-any.whl")
    os.system("pip install APScheduler-3.6.0-py2.py3-none-any.whl")

    print "***********Complete!*********"
