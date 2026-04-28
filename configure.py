#!/usr/bin/env python3
q='192.168.8.100'
p='models/garbage-yolo11s_rknn_model'
o='models/yoloe-11l-seg_rknn_model'
n='local_ip'
m='draw'
l='always_send_frames'
k='show'
j='livestream'
i='datasend_interval'
h='heartbeat_interval'
g='inference_interval'
f='overlap_iou_threshold'
e='person_iou_threshold'
d='yolo'
c='yoloe'
b='clean1'
a='rknn_garbage.py'
X='e5oNH8Yhx8eJml4bSxYw'
W='https://hajjdrf.aihajjservices.com/camera/create-camera-heartbeat/'
V='https://hajjdrf.aihajjservices.com/camera/create-garbage-monitoring/'
U='rtsp://admin:j40a@234@192.168.8.201:554/Streaming/Channels/101'
T='demo/Garbage-2.mp4'
S='='
R=int
Q=Exception
P='streams'
O='demo'
N='y'
M='X-Secret-Key'
L='heartbeat_url'
K='data_send_url'
J='sn'
I='video_source'
H=bool
G='local_video'
F='local_video_source'
D=True
C=False
B=print
import json as Y,os,sys as E
from pathlib import Path
class A:RED='\x1b[0;31m';GREEN='\x1b[0;32m';YELLOW='\x1b[1;33m';BLUE='\x1b[0;34m';PURPLE='\x1b[0;35m';CYAN='\x1b[0;36m';WHITE='\x1b[1;37m';NC='\x1b[0m'
Z=D
r='Garbage Detection System'
s='config.json'
t=a
w=a
class u:
	def __init__(A):A.config_file=s;A.config={};A.is_multi_instance=C;A.num_instances=1
	def print_header(C):B(f"{A.BLUE}{S*50}{A.NC}");B(f"{A.BLUE}  {r} Configuration Tool{A.NC}");B(f"{A.BLUE}{S*50}{A.NC}");B(f"{A.YELLOW}Multi-instance support: {'Yes'if Z else'No'}{A.NC}");B()
	def load_existing_config(E):
		if os.path.exists(E.config_file):
			try:
				with open(E.config_file,'r')as F:E.config=Y.load(F)
				B(f"{A.GREEN}Loaded existing configuration from {E.config_file}{A.NC}");return D
			except Q as G:B(f"{A.RED}Error loading config file: {G}{A.NC}");return C
		else:B(f"{A.YELLOW}No existing configuration found. Will create new one.{A.NC}");return C
	def get_user_input(I,prompt,default_value='',input_type=str):
		F=input_type;E=prompt;C=default_value
		if C:G=f"{E} [{C}]: "
		else:G=f"{E}: "
		D=input(G).strip()
		if not D and C:return C
		if F==H:return D.lower()in[N,'yes','true','1']
		elif F==R:
			try:return R(D)if D else C
			except ValueError:B(f"{A.RED}Invalid number, using default: {C}{A.NC}");return C
		return D if D else C
	def configure_multi_instance(E):
		if not Z:return C
		B(f"\n{A.CYAN}Multi-Instance Configuration{A.NC}");B('This project supports running multiple instances simultaneously.');F=E.get_user_input('Do you want to run multiple instances? (y/N)','n',H)
		if F:
			E.is_multi_instance=D;E.num_instances=E.get_user_input('How many instances do you want to run?',2,R)
			if E.num_instances<1:E.num_instances=1
			B(f"{A.GREEN}Configured for {E.num_instances} instances{A.NC}");return D
		return C
	def configure_basic_settings(E):
		B(f"\n{A.CYAN}Basic Configuration{A.NC}");F=E.get_user_input('Do you want to update the configuration? (Y/n)',N,H)
		if not F:B(f"{A.YELLOW}Using default configuration. Demo video will be used.{A.NC}");B(f"{A.YELLOW}To change video source, run this script again and choose to update config.{A.NC}");return C
		return D
	def configure_video_source(K,stream_config=None):
		E=stream_config
		if E is None:E={}
		L=E.get(F,T);P=E.get(I,U);Q=E.get(J,b);B(f"{A.PURPLE}Video Source Configuration{A.NC}");B(f"Current demo video: {A.YELLOW}{L}{A.NC}");R=K.get_user_input('Use demo video or camera? (demo/camera)',O)
		if R.lower()in[O,'d']:
			E[G]=D;S=K.get_user_input(f"Use default demo video? (Y/n)",N,H)
			if not S:V=K.get_user_input('Enter demo video path',L);E[F]=V
			else:E[F]=L
			B(f"{A.GREEN}Using demo video: {E[F]}{A.NC}")
		else:E[G]=C;M=K.get_user_input('Enter RTSP URL',P);E[I]=M;B(f"{A.GREEN}Using camera: {M}{A.NC}")
		W=K.get_user_input('Enter device serial number (sn)',Q);E[J]=W;return E
	def configure_api_settings(C):B(f"\n{A.CYAN}API Configuration{A.NC}");D=C.config.get(K,V);E=C.config.get(L,W);F=C.config.get(M,X);G=C.get_user_input('Enter data send URL',D);H=C.get_user_input('Enter heartbeat URL',E);I=C.get_user_input('Enter X-Secret-Key',F);C.config[K]=G;C.config[L]=H;C.config[M]=I
	def create_single_instance_config(E):B(f"\n{A.GREEN}Configuring Single Instance{A.NC}");H={c:o,d:p,e:.3,f:.7,g:10,h:3,i:9,O:C,j:D,k:C,l:D,m:C,G:D,F:T,I:U,K:V,L:W,M:X,n:q,J:b};E.config={**H,**E.config};E.config=E.configure_video_source(E.config);E.configure_api_settings()
	def create_multi_instance_config(E):
		if E.is_multi_instance:B(f"\n{A.GREEN}Configuring Multi-Instance ({E.num_instances} instances){A.NC}")
		else:B(f"\n{A.GREEN}Configuring Single Instance (using multi-instance structure){A.NC}")
		H={c:o,d:p,e:.3,f:.7,g:10,h:3,i:9,O:C,j:D,k:C,l:D,m:C,K:V,L:W,M:X,n:q,P:[]}
		if hasattr(E,'config')and E.config:
			for(N,Y)in H.items():
				if N not in E.config or N==P:E.config[N]=Y
			H=E.config
		R=[]
		for S in range(E.num_instances):B(f"\n{A.PURPLE}Configuring Stream {S+1}/{E.num_instances}{A.NC}");Q={J:f"clean{S+1}",G:D,I:U,F:T};Q=E.configure_video_source(Q);R.append(Q)
		H[P]=R;E.config=H;E.configure_api_settings()
	def save_configuration(E):
		try:
			with open(E.config_file,'w')as F:Y.dump(E.config,F,indent=4)
			B(f"\n{A.GREEN}Configuration saved to {E.config_file}{A.NC}");return D
		except Q as G:B(f"\n{A.RED}Error saving configuration: {G}{A.NC}");return C
	def display_summary(D):
		C='N/A';B(f"\n{A.CYAN}Configuration Summary{A.NC}");B(f"{A.YELLOW}{S*40}{A.NC}");H=D.config.get(P,[])
		if D.is_multi_instance:B(f"Mode: {A.GREEN}Multi-Instance ({D.num_instances} streams){A.NC}")
		else:B(f"Mode: {A.GREEN}Single Instance (using multi-instance structure){A.NC}")
		B(f"Script to use: {A.YELLOW}{t}{A.NC}")
		for(N,E)in enumerate(H):
			B(f"\nStream {N+1}:");B(f"  Serial Number: {A.CYAN}{E.get(J,C)}{A.NC}");B(f"  Local Video: {A.CYAN}{E.get(G,C)}{A.NC}")
			if E.get(G):B(f"  Demo Video: {A.CYAN}{E.get(F,C)}{A.NC}")
			else:B(f"  RTSP Source: {A.CYAN}{E.get(I,C)}{A.NC}")
		B(f"\nAPI Configuration:");B(f"  Data URL: {A.CYAN}{D.config.get(K,C)}{A.NC}");B(f"  Heartbeat URL: {A.CYAN}{D.config.get(L,C)}{A.NC}");B(f"  Secret Key: {A.CYAN}{D.config.get(M,C)}{A.NC}")
	def run(E):
		E.print_header();E.load_existing_config()
		if E.configure_multi_instance():E.create_multi_instance_config()
		else:E.num_instances=1;E.is_multi_instance=C;E.create_multi_instance_config()
		E.display_summary();B(f"\n{A.YELLOW}Review the configuration above.{A.NC}");F=E.get_user_input('Save this configuration? (Y/n)',N,H)
		if F:
			if E.save_configuration():B(f"\n{A.GREEN}Configuration completed successfully!{A.NC}");B(f"{A.YELLOW}You can now run: ./run-project.sh{A.NC}");return D
			else:B(f"\n{A.RED}Failed to save configuration.{A.NC}");return C
		else:B(f"\n{A.YELLOW}Configuration cancelled.{A.NC}");return C
def v():
	try:C=u();D=C.run();E.exit(0 if D else 1)
	except KeyboardInterrupt:B(f"\n{A.YELLOW}Configuration cancelled by user.{A.NC}");E.exit(1)
	except Q as F:B(f"\n{A.RED}Unexpected error: {F}{A.NC}");E.exit(1)
if __name__=='__main__':v()