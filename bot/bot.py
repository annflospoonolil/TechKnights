from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
TOKEN: Final ="7187640848:AAGtBYzsXdK8BybHR7_Qq2CN0YFwZWpYjLI"
BOT_USERNAME : Final = '@poschy'

import json
import requests




# with open("data.json", "r") as file:
#     data = json.load(file)
# json_formatted_string = json.dumps(data)


#commands
async def start_command(update : Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for choosing me!')           

async def help_command(update : Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I will help you find the suitable investor for your idea,type investor!')

 

async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bot terminated!')
      

    # responses 

def handle_response(text:str) -> str:
    processed: str = text.lower().strip()

    # Define the API endpoint URL
    url = "http://192.168.155.245:5000/data"

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()
        print(data)  # Do something with the data
    else:
        # Print an error message if the request was not successful
        print(f"Failed to fetch data: {response.status_code}")
    
    # if 'investor' in processed:
        
    #     l = set()  # Initialize an empty set
    #     for i in data:
    #         if 'topic' in i:
    #             l.add(str(i['topic']))  # Add each topic to the set
    #     return ', '.join(l)
    #if 'investor' in processed:
    #    topics_set = set()  # Initialize an empty set
    #    for i in data:
    #        if 'topic' in i:
    #            topics_set.add(str(i['topic']))  # Add each topic to the set
    #    topics_string = '\n'.join(topics_set)
    #    return "Choose your interest field:\n" + topics_string
    if 'investor' in processed:
        topics_set = set()  # Initialize an empty set
        for i in data:
            if 'topic' in i:
               topics_set.add(str(i['topic']))  # Add each topic to the set
        sorted_topics = sorted(topics_set)  # Sort the topics alphabetically
    
        topics_with_numbers = "\n".join(f"{index+1}. {topic}" for index, topic in enumerate(sorted_topics))
    
        return "Choose your interest field:\n" + topics_with_numbers


    

    
    
    #if 'technology' in processed:
    #    donation = set()  # Initialize an empty set
    #    for i in data:
    #        if 'donation' in i:
    #            donation.add(str(i['donation']))  # Add each topic to the set
    #    donation_string = '\n'.join(donation)
    #    return "Choose required investment range for your:\n" + donation_string
    if 'technology' ==processed or '3' == processed:
        print("3" in processed,type(processed),"value")
        unique_donations = set()  # Initialize an empty set for unique donations
        for investor in data:
            if 'technology' in investor.get('topic', '').lower():
                donation = investor.get('donation', 'Not specified')
                unique_donations.add(donation)  # Add each donation to the set
        sorted_donations = sorted(unique_donations)  # Sort the unique donations
        donation_string = '\n'.join(sorted_donations)
        return "Choose required investment range for technology:\n" + donation_string

   
      
    #elif 'healthcare' in processed:
    #    donations = set()
    #    for investor in data:
    #        if 'healthcare' in investor.get('topic', '').lower():
    #            donation = investor.get('donation', 'Not specified')
    #            donations.add(donation)
    #    donation_string = '\n'.join(donations)
    #    return "Choose required investment range for Healthcare:\n" + donation_string
    elif 'healthcare' == processed or '1' == processed:
        unique_donations = set()  # Initialize an empty set for unique donations
        for investor in data:
            if 'healthcare' in investor.get('topic', '').lower():
                donation = investor.get('donation', 'Not specified')
                unique_donations.add(donation)  # Add each donation to the set
        sorted_donations = sorted(unique_donations)  # Sort the unique donations
        donation_string = '\n'.join(sorted_donations)
        return "Choose required investment range for Healthcare:\n" + donation_string

    
    #elif 'renewable energy' in processed:
        # Extract donation_min for each investor with 'technology' as topic
    #    donations = set()
    #    for investor in data:
    #        if 'renewable energy' in investor.get('topic', '').lower():
    #            donation = investor.get('donation', 'Not specified')
    #            donations.add(donation)
    #    return '\n'.join(donations)
    elif 'renewable energy' == processed or '2' == processed:
        
        unique_donations = set()  # Initialize an empty set for unique donations
        for investor in data:
            if 'renewable energy' in investor.get('topic', '').lower():
                donation = investor.get('donation', 'Not specified')
                unique_donations.add(donation)  # Add each donation to the set
        sorted_donations = sorted(unique_donations)  # Sort the unique donations
        donation_string = '\n'.join(sorted_donations)
        return "Choose required investment range for renewable energy:\n" + donation_string


    
    if ('1-10lakhs' in processed) or ('10-20lakhs' in processed) or ('20-30lakhs' in processed) or ('30-40lakhs' in processed ) or ('40-50lakhs' in processed):
         
        return "Good! confirm your choice  (eg: tech,1-10)"
        
    
    if 'tech,1-10' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'tech,1-10':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
    
    if 'tech,10-20' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'tech,10-20':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
        
    if 'tech,20-30' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'tech,20-30':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."    

    
    if 'tech,30-40' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'tech,30-40':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
             
    if 'tech,40-50' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'tech,40-50':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."


    if 'heal,1-10' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,1-10':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
    if 'heal,10-20' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,10-20':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
        
    if 'heal,20-30' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,20-30':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."    

    
    if 'heal,30-40' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,30-40':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
             
    if 'heal,40-50' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,40-50':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found." 
    if 'rene,1-10' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,1-10':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
    if 'rene,10-20' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,10-20':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
        
    if 'rene,20-30' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,20-30':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."    

    
    if 'rene,30-40' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,30-40':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."
             
    if 'rene,40-50' in processed:
        matching_investors = []
        for investor in data:
            if 'final_des' in investor and investor['final_des'] == 'heal,40-50':
                matching_investors.append(investor)
        
        if matching_investors:
            response = ""
            for investor in matching_investors:
                response += f"Name: {investor.get('name', 'N/A')}\n"
                response += f"Location: {investor.get('location', 'N/A')}\n"
                response += f"Startup Size: {investor.get('startup_size', 'N/A')}\n"
                response += f"Description: {investor.get('description', 'N/A')}\n"
                response += f"Email-id :{investor.get('email','N/A')}\n"
                response += f"LinkedIn :{investor.get('linkedin','N/A')}\n\n"
            return response
        else:
            return "No matching investors found."      


    
    

    return ' I do not understand what you wrote..'
    

async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type: str= update.message.chat.type
    text:str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str=text.replace(BOT_USERNAME,'').strip()
            response : str = handle_response(new_text)
        else:
            return
    else:
        response :str=handle_response(text)   

    print('Bot:',response) 
    await update.message.reply_text(response) 

async def error(update : Update,context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__=='__main__':
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('exit', exit_command))

    #message
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #error
    app.add_error_handler(error)

    #polls the bot

    print('Polling...')
    app.run_polling(poll_interval=3)

        