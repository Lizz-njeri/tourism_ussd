from flask import Flask, request
import africastalking
import os


app = Flask(__name__)
username = "Kwepo"
api_key = "f67c169248ae4bf36bdc9e798afed8428dcd3770bf78cf051d4faa752fd8a8a9"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])

def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    #ussd logic
    if text == "":
        #main menu
        response = "CON Hello there adventurer,\n Where do you want to be today?\n"
        response += "1. Game Parks and Reserves\n"
        response += "2. Museums\n"
        response += "3. Recreational Parks\n"
        response += "4. National Conservatives\n"
        response += "5. Nature Trails\n"


    elif text == "1":
        #sub menu 1
        response = "CON Available Game parks and reserves\n"
        response += "1. Giraffe Center\n"
        response += "2. Nairobi National Park\n"
        response += "3. Nairobi Snake Park and Aquarium\n"
        response += "4. Mamba Village\n"
        response += "5. Nairobi Orphanage\n"
        response += "6. Nairobi Elephant Sanctuary\n"     
    elif text == "2":
        response ="CON Available Museums\n"
        response += "1. National Musem\n"
        response += "2. Karen Blixen Museum\n"
        response += "3. Kenya Railway Museum\n"
    elif text == "3":
        response = "CON Available Recreational parks"
        response += "1. Uhuru Park\n"
        response += "2. National Aboretum"
        response += "3. Central Park\n"
        response += "4. City Park Shop\n"
       
    elif text == "4":
        response = "CON Available National conservatives"
        response += "1. National Archives\n"
        response += "2. National Gallery\n"
        response += "3. Bomas of Kenya\n"
    elif text == "5":
        response = "CON Available nature trails"
        response += "1. Ngong Hills\n"
        response += "2. Karura Forest\n"
        response += "3. Oloolua Nature Trail\n"
        response += "4. Ngong Road Forest Sanctuary\n"

    
    elif text == "1*1":
        response = "END We have sent you sms details on the selected adventure\n"
        sms.send("Time: 9AM to 5PM\n Entry Fee: Residents Adults-400, Kids-200. Non-residents Adults-1500, Kids-750.\n For schools, its free entry with 1-week advance booking.\n Location: Giraffe centre, Duma road, Nairobi", sms_phone_number)
    elif text == "1*2":
        response = "END We have sent you sms details on the selected adventure\n"
        sms.send("Time: 6AM to 7PM\n Entry fee: Adults-430, Kids-215.\n Location: Langata Road, Nairobi",sms_phone_number)
    elif text == "1*3":
        response = "END We have sent you sms details on the selected adventure\n"
        sms.send("Time: 9AM to 5:30PM \n Entry fee: Citizens: Adults-200, Kids-100 \nEast African: Adults-400, Kids-200\n Non-Resident : Adults-1200, Kids-600.\n Location:Museum Hill, Nairobi",sms_phone_number)
    elif text == "1*4":
        response = "END We have sent you sms details on the selected adventure\n"
        sms.send("Time: 9AM to 6PM \n Entry fee:Adults-200\n Activities: Boat ride, Horse ride, Camel Riding.", sms_phone_number)
    elif text == "1*5":
        response = "END We have sent you sms details on the selected adventure\n"
        sms.send("Time: 8AM to 5PM \n Entry fee: Adults-2000, Kids-500\n Location:National Park, Karen, Langata Rd, Nairobi", sms_phone_number)
    elif text == "1*6":
        response = "END We have sent you sms details on the selected adventure\n"
        sms.send("Time: 11AM to 12PM\n Entry fee:Adults-1500. \n Location: Mbagathi Gate, Off Magadi Road,KWS Workshop Entrance-Nairobi National Park, Nairobi",sms_phone_number)

    
    elif text == "2*1":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time: 9AM to 5:30PM \n Entry fee: Citizens: Adults-200, Kids-100 \nEast African: Adults-400 Kids-200\n Non-Resident : Adults-1200, Kids-600.\n Location:Museum Hill, Nairobi",sms_phone_number)
    elif text == "2*2":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time:8:30AM to 6PM \n Entry fee: Citizens: Adults-200, Kids-100 \n East African: Adults-600, Kids-400\n Non-Resident: Adults-1200, Kids-600\n Location:Karen Road, Nairobi",sms_phone_number)
    elif text == "2*3":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time: 8AM to 5pm \n Entry fee: Citizen: Adults -200, Kids/Students-100 \n East African: 500\n Non-Resident:Adults-600, Students-300, Kids-100",sms_phone_number)

    
    elif text == "3*1":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time: 9AM to 6PM \n Entry fee: Free but have a national ID/passport",sms_phone_number)
    elif text == "3*2":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time:6AM to 6PM \n Entry fee:Adults-65, Kids-27 \n Location:Kilimani Aboretum Road, off State House Road, Nairobi",sms_phone_number)
    elif text == "3*3":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time:9AM to 6PM\n Entry fee: Free\n Location:Kenyatta Avenue, Nairobi",sms_phone_number)
    elif text == "3*4":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time:9AM to 6PM \n Entry fee:Free ",sms_phone_number)
    
    
    elif text == "4*1":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time:9AM to 5PM \n Entry fee: Non residents: Adults-200 \n Citizens: Adults:50 \n Location: Moi Avenue, Nairobi",sms_phone_number)
    elif text == "4*2":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time: 8:30AM to 6PM \n Entry fee: Citizens:Adults-150, Kids-100, East African: Adults -600, Kids -400, Non- Residents:Adults -1000, Kids-500 \n Location: Kenyatta Avenue, Nairobi",sms_phone_number)
    elif text == "4*3":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time: 2:30PM to 4PM \n Entry fee: Citizens: Adults -200, Kids-50 \n East African:Adults-300, Kids-200\n Non-residents:Adults-1000, Kids-500\n Location:Langata road, Mageso Chember, Nairobi",sms_phone_number)

    elif text == "5*1":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Entry fee:480 \n Location:Ngong town",sms_phone_number)
    elif text == "5*2":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time: 6AM to 6PM \n Entry fee: Citizen:Adults-100, Kids-50 \n East African:Adults-200, Kids-100\n Non-resident: Adults-600, Kids-300 \n Location:Limuru road, Nairobi",sms_phone_number)
    elif text == "5*3":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time:9AM to 6PM \n Entry fee:Citizens:Adults-200, Kids-100\n East African: Adults-400, Kids-200\n Non-Residents:Adults-600, Kids-300\n Location:Karen Rd, Nairobi",sms_phone_number)
    elif text == "5*4":
        response ="END We have sent you sms details on the selected adventure"
        sms.send("Time: 6AM to 6PM\n Entry fee:Adults-100, Kids-50 \nLocation:Ngong road, Ngong",sms_phone_number)
   

    else:
        response = "END Invalid response."

    return response




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))