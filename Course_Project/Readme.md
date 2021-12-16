# Programming For Cybersecurity course - Project

##  Course Project
## Description:
Complete a project that demonstrates your knowledge of programming in some area of cybersecurity. This is deliberately vague to allow you to create your own project. This can be a project that you need to complete for work.


## Author: Tomasz
## Subject: Development of a buffer overflow exploit based on a proof of concept exploit.

The project assumes that as a result of a network reconnaisanse a vulnerable software has been identified on a remote host. The remote machine is running Seattle Lab Mail Software version 5.5. The author of this project will be presenting steps required to confirm the target is vulnerable, outline steps needed to develop in a lab envirnment a fully functional exploit including a payload which can be used to obtain command line access to the targeted machines. The vulnerable software can be downloaded from the exploit-db link in references. Each stage of exploitation process requires an individual python script which will a result of modification made based on result of previous step.

## STEPS TO REPRODUCE:
STEP 1 - Cause a crash by interacting with the exposed port.

STEP 2 - Identify EIP register position.

STEP 3 - Identify available space for shellcode.

STEP 4 - Examine Shellcode for bad character.

STEP 5 - Find instruction to which execution of application needs to be reditected (to our malicious code).

STEP 6 - Generating a shellcode and updating the exploit.

STEP 7 - Exploitation phase.


## STEP 1 - Cause a crash by interacting with the exposed port

[step1_fuzzer.py](https://github.com/kodkoder/p4cs2021/blob/main/Course_Project/step1_fuzzer.py)

## STEP 2 - Identify EIP register position

[step2_eip.py](https://github.com/kodkoder/p4cs2021/blob/main/Course_Project/step2_eip.py)

## STEP 3 - Identify available space

[step3_space.py](https://github.com/kodkoder/p4cs2021/blob/main/Course_Project/step3_space.py)

## STEP 4 - Examine Shellcode for bad character

[step4_bad_char.py](https://github.com/kodkoder/p4cs2021/blob/main/Course_Project/step4_bad_char.py)

## STEP 5 - Find instruction to which execution of application needs to be reditected (to our malicious code)

[step5_jmp_esp.py](https://github.com/kodkoder/p4cs2021/blob/main/Course_Project/step5_jmp_esp.py)

## STEP 6 - Generating a shellcode and updating the exploit

[step6_shellcode.py](https://github.com/kodkoder/p4cs2021/blob/main/Course_Project/step6_shellcode.py)

## STEP 7 - Exploitation phase

[step7_exploit_final.py](https://github.com/kodkoder/p4cs2021/blob/main/Course_Project/step7_exploit_final.py)


## References:

https://cwe.mitre.org/top25/archive/2021/2021_cwe_top25.html - 2021 CWE Top 25 Most Dangerous Software Weaknesses

https://cwe.mitre.org/data/definitions/119.html  - CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer

https://nvd.nist.gov/vuln/detail/CVE-2003-0264 - Buffer overflow in SLMail - CVE details

https://www.exploit-db.com/exploits/638 - POC exploit

https://github.com/R4v3nG/Seattle-Lab-Mail-SLmail-5.5-POP3-PASS-Remote-Buffer-Overflow
