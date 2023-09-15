def generate_mail(OTP, rainfall=1):
    mail_content = f"""\
            <html>

            <head>
                <div style="font-weight: 1000; color: white;"><u>Rainfall Prediction Result</u></div>
            </head>
            
            <body style="background-color: black; text-align: center;">
                <br> <a href="#">
                
                <p style="color: green;">
                    <b>
                        Hello, this is an automated message from the MedLib!
                    </b>
                </p>
                <p>
                <div style="color: white">
                    Your OTP is: <br>
                </div>
                <div style="color: goldenrod; font-weight: 520;">
                    Your OTP is: {OTP}
                </div>
                </p>
                <p style="color: red; font-weight: 750;">
                    
                </p>
                <p style="color: white;">
                    (Feel free to leave us feedback on our
                    <a href="mailto:archmages.neural@gmail.com?
                                &cc=
                                &bcc=
                                &subject=OTP for MedLib
                                &body=Add whatever suggestions or message you would like to send here" 
                                target="_blank">
                        Mail
                    </a> or our
                    <a href="https://github.com/PalakDwivedi02/Rainfall-Prediction-using-ML" target="_blank"> Github Page</a>!)
                </p>
                <p>
                <div style="color: limegreen;">
                    Thank you for using our service!
                </div>
                <div style="color: white; font-weight: 750;"> <br>
                     
                    <div style="color:red">MedLib</div>
                </div>
                </p>
            </body>
            
            </html>
        """  # .format(month, day, temp, sphum, relhum, rainfall)
    return mail_content
