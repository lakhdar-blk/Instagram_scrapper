import instaloader
import xlsxwriter


def insta_srcapping(username, password, target, insta_list, file_name, location):

    row = 0 

    try:
        
        workbook = xlsxwriter.Workbook(location+"/"+file_name)
        worksheet = workbook.add_worksheet()

        worksheet.write(row, 0, "Followers")
        worksheet.set_column(row, 0, 50)

        worksheet.write(row, 1, "Following")
        worksheet.set_column(row, 1, 50)

        row += 1

    except Exception as error:
        
        return(error)

    try:

        L = instaloader.Instaloader()

        L.login(username, password)

        profile = instaloader.Profile.from_username(L.context, target)


        if(insta_list == 0):
            
            for follower in profile.get_followers():

                worksheet.write(row, 0, follower.username)
                row +=  1

        elif(insta_list == 1):

            for following in profile.get_followees():

                worksheet.write(row, 1, following.username)
                row +=  1

        elif(insta_list == 2):
            
            for follower in profile.get_followers():

                worksheet.write(row, 0, follower.username)
                row +=  1

            row = 1

            for following in profile.get_followees():

                worksheet.write(row, 1, following.username)
                row +=  1
        
        workbook.close()
        return "Operation Success !"
    except Exception as error:
        
        return(error)
    


#insta_srcapping("android_games_dz", "Ghali1956", "android_games_dz", 2)