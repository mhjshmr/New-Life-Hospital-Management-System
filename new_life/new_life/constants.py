from django.forms import fields
from phonenumber_field import formfields

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
)

BLOOD_GROUPS = (
    ("A+",) * 2,
    ("A-",) * 2,
    ("B+",) * 2,
    ("B-",) * 2,
    ("O+",) * 2,
    ("O-",) * 2,
    ("AB+",) * 2,
    ("AB-",) * 2,
)
WORKING_HOURS = (
    ("08:00-13:00", "Morning"),
    ("13:00-18:00", "Noon"),
    ("18:00-00:00", "Night"),
)

CATEGORIES = (
    ("D", "Doctor"),
    ("P", "Patient"),
    ("S", "Staff"),
)

GROUPS = ["Doctors", "Patients", "Staffs"]
PERMISSIONS = {
    "Doctors": [
        "add_appointment",
        "change_appointment",
        "delete_appointment",
        "view_appointment",
        "view_department",
        "change_doctor",
        "view_patient",
        "view_lab",
        "add_medicalrecord",
        "change_medicalrecord",
        "view_medicalrecord",
        "delete_medicalrecord",
        "add_prescription",
        "change_prescription",
        "delete_prescription",
        "view_prescription",
        "add_xray",
        "change_xray",
        "delete_xray",
        "view_xray",
        "view_role",
        "view_staff",
    ],
    "Patients": [
        "add_appointment",
        "change_appointment",
        "delete_appointment",
        "view_appointment",
        "view_department",
        "view_patient",
        "view_lab",
        "view_medicalrecord",
        "view_prescription",
        "view_xray",
        "view_role",
        "view_staff",
    ],
    "Staffs": [
        "add_appointment",
        "change_appointment",
        "delete_appointment",
        "view_appointment",
        "add_department",
        "change_department",
        "delete_department",
        "view_department",
        "add_doctor",
        "change_doctor",
        "delete_doctor",
        "view_doctor",
        "add_patient",
        "change_patient",
        "delete_patient",
        "view_patient",
        "add_lab",
        "change_lab",
        "delete_lab",
        "view_lab",
        "view_medicalreport",
        "view_prescription",
        "add_xray",
        "change_xray",
        "delete_xray",
        "view_xray",
        "add_role",
        "change_role",
        "delete_role",
        "view_role",
        "add_staff",
        "change_staff",
        "delete_staff",
        "view_staff",
    ],
}

REGISTRATION_FIELDS = [
    "first_name",
    "last_name",
    "username",
    "email",
    "password",
    "profile_pic",
    "date_of_birth",
    "phone_number",
    "gender",
    "blood_group",
    "address",
    "eid",
]
SIGN_UP_LAYOUT = [
    ['X', 'X'],
    ['X', 'X'],
    ['X', 'X'],
    ['X', 'X'],
    ['X', 'X'],
    ['X', 'X'],
    ['X'],
    ['X'],
]
WIDGET_ATTRS = {
    fields.CharField: {
        "class": "block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer",
        "placeholder": " "
    },
    fields.EmailField: {
        "class": "block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer",
        "placeholder": " "
    },
    fields.ImageField: {
        "class": "block w-full text-sm text-gray-400 bg-gray-50 rounded-lg border border-gray-300 cursor-pointer dark:text-gray-400 focus:outline-none dark:bg-gray-900 dark:border-gray-600 dark:placeholder-gray-400"
    },
    fields.DateField: {
        "datepicker": True,
        "datepicker-autohide": True,
        "datepicker-format": "yyyy-mm-dd",
        "datepicker-orientation": "top",
        "datepicker-title": "Date of Birth",
        "type": "text",
        "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
        "placeholder": "Select date",
        "required": True
    },
    fields.TypedChoiceField: {
        "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
        "required": True
    },
    formfields.PhoneNumberField: {
        "type": "tel",
        "name": "phone_number",
        "id": "phone_number",
        "class": "block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer",
        "placeholder": " ",
        "required": True
    },
}
"""
Can add log entry add_logentry
Can change log entry change_logentry
Can delete log entry delete_logentry
Can view log entry view_logentry
Can add appointment add_appointment
Can change appointment change_appointment
Can delete appointment delete_appointment
Can view appointment view_appointment
Can add group add_group
Can change group change_group
Can delete group delete_group
Can view group view_group
Can add permission add_permission
Can change permission change_permission
Can delete permission delete_permission
Can view permission view_permission
Can add content type add_contenttype
Can change content type change_contenttype
Can delete content type delete_contenttype
Can view content type view_contenttype
Can add department add_department
Can change department change_department
Can delete department delete_department
Can view department view_department
Can add doctor add_doctor
Can change doctor change_doctor
Can delete doctor delete_doctor
Can view doctor view_doctor
Can add patient add_patient
Can change patient change_patient
Can delete patient delete_patient
Can view patient view_patient
Can add lab add_lab
Can change lab change_lab
Can delete lab delete_lab
Can view lab view_lab
Can add medical report add_medicalreport
Can change medical report change_medicalreport
Can delete medical report delete_medicalreport
Can view medical report view_medicalreport
Can add prescription add_prescription
Can change prescription change_prescription
Can delete prescription delete_prescription
Can view prescription view_prescription
Can add x ray add_xray
Can change x ray change_xray
Can delete x ray delete_xray
Can view x ray view_xray
Can add session add_session
Can change session change_session
Can delete session delete_session
Can view session view_session
Can add role add_role
Can change role change_role
Can delete role delete_role
Can view role view_role
Can add staff add_staff
Can change staff change_staff
Can delete staff delete_staff
Can view staff view_staff
Can add user add_userprofile
Can change user change_userprofile
Can delete user delete_userprofile
Can view user view_userprofile
"""
