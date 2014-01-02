<!DOCTYPE html>
<html>
<head>
<title>
Mail
</title>
<style type="text/css">
#fixed{
width:300%;
}
</style>
</head>
<body>
<p>Mass mailer requires your Gmail access credentials for sending mails</p>
<form action="/mass_mail" method="POST">
<table>
<tr><td>Username: <input type="text" name="name" value=""><br></td><tr>
<tr><td>Password:&nbsp;&nbsp;<input type="password" name="password" value=""><br></td><tr>
<tr><td>FromAddr: <input type="text" name="fromaddr" value=""><br></td><tr>
<tr><td style="white-space:nowrap;">Mail To :&nbsp;&nbsp;&nbsp;<input type="text"  name="P_Email" style="width:300%"  value={{','.join(str(e) for e in emails.values())}} disabled></td><br><tr>
<tr><td><input type="hidden" name="P_UID" value={{','.join(str(e) for e in emails.keys())}}><br></td><tr>
<tr><td style="white-space:nowrap;">Subject:&nbsp;&nbsp;&nbsp;<input type="text" name="subject" maxlength="1000" style="height:25px;width:300%"></td></tr>
<div>
<br>
<tr><td style="word-wrap:break-word;">Message:</td></tr>
<tr><td><TEXTAREA name="message" size="238" rows="10" style="height:100px;width:324%;"></TEXTAREA></td></tr>
</br>
</div>
<tr><td><input type="submit" value="Submit"></td>
</div>
</form>
</body>
</html>

