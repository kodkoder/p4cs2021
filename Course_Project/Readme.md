# Programming For Cybersecurity course - Prokect

##  Course Project
### Description:
Complete a project that demonstrates your knowledge of programming in some area of cybersecurity. This is deliberately vague to allow you to create your own project. This can be a project that you need to complete for work.


### Author: Tomasz
### Subject: Development of a buffer overflow exploit based on a proof of concept payload.

The project assumes that as a result of a network reconnaisanse a vulnerable software has been identified on a remote host. The remote machine is running Seattle Lab Mail Software version 5.5. The author of this project will be presenting steps required to confirm the target is vulnerable, outline steps needed to develop in a lab envirnment a fully functional exploit including a payload which can be used to obtain command line access to the targeted machines. The vulnerable software can be downloaded from the exploit-db link in references. Each stage of exploitation process requires an individual python script which will a result of modification made based on result of previous step

### STEPS TO REPRODUCE:
STEP 1 - Cause a crash by interacting with the exposed port
STEP 2 - Identify EIP register position
STEP 3 - Identify available space
STEP 4 - Examine Shellcode for bad character
STEP 5 - Find instruction to which execution of application needs to be reditected (to our malicious code)
STEP 6 - Generating a shellcode and updating the exploit
STEP 7 - Exploitation phase


### Code:
[bmi.py](https://github.com/kodkoder/p4cs2021/blob/main/Project/fuzzer.py)

## STEP 1 - Cause a crash by interacting with the exposed port
### Code:
[bmi.py](https://github.com/kodkoder/p4cs2021/blob/main/Project/fuzzer.py)

## STEP 2 - Identify EIP register position
## STEP 3 - Identify available space
## STEP 4 - Examine Shellcode for bad character
## STEP 5 - Find instruction to which execution of application needs to be reditected (to our malicious code)
## STEP 6 - Generating a shellcode and updating the exploit
## STEP 7 - Exploitation phase



###References:
https://nvd.nist.gov/vuln/detail/CVE-2003-0264 - Buffer overflow
https://www.exploit-db.com/exploits/638 - POC exploit
https://github.com/R4v3nG/Seattle-Lab-Mail-SLmail-5.5-POP3-PASS-Remote-Buffer-Overflow
