<?php 
	$responses['what is your name'] = "My name is HNG bot.";
	// echo "Hello world";
	$responses['tell me about yourself'] = "I am a chatbot. I'm still learning a lot of things so please forgive me if I can't answer you in some cases.";
	
	$responses["i'm fine"] = "Good. I'm happy about that.";
	$q = $_GET["q"];

	$response = "";

	if ($q != "") {
		# code...
		$q = strtolower($q);
		foreach ($responses as $r => $value) {
			# code...
			if (strpos($r, $q) !== false) {
				# code...
				$response = $value;
			}
			
		}
	}
	$noresponse = "Sorry I'm still learning. Hence my responses are limited. Ask something else.";
	echo $response === "" ? $noresponse : $response;
?>


userr = users.drop(['email','image','provider','provider_id','password','remember_token','created_at','updated_at','short_bio'],axis=1)
contact_settings = contact_settings.drop(['email','display_message','created_at','updated_at'],axis=1)