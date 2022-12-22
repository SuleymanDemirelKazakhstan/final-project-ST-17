import telebot
from telebot import types

bot = telebot.TeleBot('5941463029:AAGjycDegxAvLuiSNUa1Lxbm0s27vhDfu_s')

#Main Menu - Admission
def main_menu_admission(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    admissions_committee = types.InlineKeyboardButton("Admissions Committee", callback_data="admissions_committee")
    master_degree = types.InlineKeyboardButton("Master's Degree/PHD", callback_data="admissions_master_degree")
    back_menu = types.InlineKeyboardButton("Go back", callback_data="back_menu")
    register = types.InlineKeyboardButton("Register in the personal cabinet!", url="https://oldmy.sdu.edu.kz/")
    markup.add(register, admissions_committee,master_degree,back_menu)
    bot.send_message(message.chat.id, '''To find the information you need, select the section you are interested in:

We also invite you to sign up for an SDU Student Profile so you don't miss out on important information about the admissions and enrollment process and save yourself time when you apply.''', reply_markup=markup)

#Main Menu - Admission - Master degree
def main_menu_admission_master(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    online_consultation = types.InlineKeyboardButton("Online Consultation", url="https://meet.google.com/yoy-bnss-ens")
    document_deadline_master = types.InlineKeyboardButton("Deadlines for submitting documents",callback_data="document_deadline_master")
    document_required_master = types.InlineKeyboardButton("Documents required for admission",callback_data="document_required_master")
    admission_rules_master = types.InlineKeyboardButton("Admission rules", callback_data="admission_rules_master")
    back_admission = types.InlineKeyboardButton("Go back",callback_data="back_admission")
    markup.add(online_consultation,document_deadline_master,document_required_master,admission_rules_master,back_admission)
    bot.send_message(message.chat.id, "Here links to the most common questions about admission for master's degree.", reply_markup=markup)

#Main Menu - Admission - Master degree - Document deadline master
def main_menu_admission_master_document_deadline_master(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_master = types.InlineKeyboardButton("Go back",callback_data="back_master")
    markup.add(back_master)
    bot.send_message(message.chat.id, '''Deadline for submitting documents

🚩June 1 - July 15 (summer), November 1-15 (autumn):
Acceptance of applications for complex testing for Master's degree.

🚩July 10 - August 20 (summer), November 18 - December 11 (winter):
Complex testing, creative exams for a Master's degree

🚩July 3 - August 3 (summer), November 1-15 ( autumn):
Acceptance of applications for PhD programs

🚩August 4-20 (summer), November 18 - December 11 ( winter):
Entry exams for PhD programs

🚩August 28 (summer), January 10 (winter):
Deadline for Masters enrollment

🚩August 28 (summer), January 10 (winter):
Deadline for PhD enrollment''', reply_markup=markup)

#Main Menu - Admission - Master degree - Document Required master
def main_menu_admission_master_document_required_master(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_master = types.InlineKeyboardButton("Go back",callback_data="back_master")
    markup.add(back_master)
    bot.send_message(message.chat.id, '''Required documents

1. Bachelor's diploma original;
2. 3x4 cm sized 6 photos
3. Medical card №075 and X-ray result (not required during lockdown);
4. Copy of National ID;
5. Copy of test certificate according to chosen program (if you have one).''', reply_markup=markup)

#Main Menu - Admission - Master degree - Admission rules master
def main_menu_admission_master_admission_rules_master(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_master = types.InlineKeyboardButton("Go back",callback_data="back_master")
    markup.add(back_master)
    bot.send_message(message.chat.id, '''Admission Rules

Applicants have to write a complex test (CT) to apply for Master's degree.
Complex testing has several parts:
1. Foreign language proficiency (not required, if you have (IELTS 6.0, TOEFL (IBT 60, PBT 498);
2. Test to identify applicant's preparation for graduate school;
3. Test on profile group subjects of educational programs.
Complex testing subjects are available here.
Complex Testing Question templates are available here.
Complex Testing trial questions are available here.
The passing score for those entering the scientific-pedagogical master's degree program is 75 points, for those entering the profile master’s degree program- 50 points .
In competition for state scholarship (grant) an applicant can choose one group of educational programs and 3.''', reply_markup=markup)



#Main Menu - Admission - Admission Committee
def main_menu_admission_committee(message):
    markup_admissions_committee = types.InlineKeyboardMarkup(row_width=1)
    online_consultation = types.InlineKeyboardButton("Online Consultation",callback_data="online_consultation")
    document_deadline = types.InlineKeyboardButton("Deadlines for submitting documents",callback_data="document_deadline")
    document_required = types.InlineKeyboardButton("Documents required for admission",callback_data="document_required")
    admission_rules = types.InlineKeyboardButton("Admission rules", callback_data="admission_rules")
    back_admission = types.InlineKeyboardButton("Go back",callback_data="back_admission")
    markup_admissions_committee.add(online_consultation,document_deadline,document_required,admission_rules,back_admission)
    bot.send_message(message.chat.id, 'Here links to the most common questions about admission.', reply_markup=markup_admissions_committee)

#Main Menu - Admission - Admission Committee - Online Consultation
def main_menu_admission_committee_online_consultation(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    online_consultation = types.InlineKeyboardButton("Online Consultation", url="https://meet.google.com/yoy-bnss-ens")
    back_admission_committee = types.InlineKeyboardButton("Go back",callback_data="back_admission_committee")
    markup.add(online_consultation,back_admission_committee)
    bot.send_message(message.chat.id, '''This consultation is intended for applicants in order to obtain information about the admission process.
Time: Every Wednesday, Thursday and Friday from 15:00 to 17:00''', reply_markup=markup)

#Main Menu - Admission - Admission Committee - Document deadline
def main_menu_admission_committee_document_deadline(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_admission_committee = types.InlineKeyboardButton("Go back",callback_data="back_admission_committee")
    markup.add(back_admission_committee)
    bot.send_message(message.chat.id, '''Deadline for submitting documents

🚩July 13 - 20:
Applications for State scholarships (grants) are accepted.

🚩June 20 - July 7:
Acceptance of documents for the creative exam

🚩July 11 - 12:
Date of the creative exam

🚩August 01 - 25:
Acceptance of documents and enrollment

🚩until August 25:
SDU examination

🚩June 20 - August 24:
Special pedagogical exams are conducted

🚩03 - 13 January:
Transfer from other universities''', reply_markup=markup)

#Main Menu - Admission - Admission Committee - Document Required
def main_menu_admission_committee_document_required(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_admission_committee = types.InlineKeyboardButton("Go back",callback_data="back_admission_committee")
    markup.add(back_admission_committee)
    bot.send_message(message.chat.id, '''Required documents

1. Copy of National ID;
2. Medical form №075 with Xray results;
3. IELTS / SDU CEC certificate if you have one or English proficiency exam result (written at SDU);
3. Applicant's 3x4cm sized, 6 photos;
7. School certificate or diploma with transcript;
8. UNT certificate (electronic copy);
9. State scholarship certificate (if you have one);
10. Special examination results (for pedagogical programs applicants);
11. Results of interview with faculty representative (for college graduates);
12. Questions for Creative exam are here;
13. Student Fund (40 000 KZT);
14. Tuition fee 50% payment.''', reply_markup=markup)

#Main Menu - Admission - Admission Committee - Admission rules
def main_menu_admission_committee_admission_rules(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_admission_committee = types.InlineKeyboardButton("Go back",callback_data="back_admission_committee")
    markup.add(back_admission_committee)
    bot.send_message(message.chat.id, '''Admission Rules

University enrollment on paid contract or scholarship is processed based on applicant's written statement, according to points t the certificate, as a result of UNT.
If you are college graduate applying to SDU, you are required to go through the interview process. ''', reply_markup=markup)