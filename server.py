from flask import Flask, request
import os
from search_and_rank import get_rank_info_and_map
from test_gmail import send_email


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def email():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            dict_values = {}
            dict_values['address'] = request.form.get('address')
            dict_values['min_cost'] = request.form.get('min_cost')
            dict_values['insurance'] = request.form.get('insurance')
            dict_values['max_cost'] = request.form.get('max_cost')
            dict_values['qualifications'] = request.form.get('qualifications')
            dict_values['specialities'] = request.form.getlist('specialities')
            dict_values['approach'] = request.form.getlist('approach')
            dict_values['p_dist'] = request.form.get('p_dist')
            dict_values['p_qual'] = request.form.get('p_qual')
            dict_values['p_ins'] = request.form.get('p_ins')
            dict_values['p_cst'] = request.form.get('p_cst')
            dict_values['p_type'] = request.form.get('p_type')
            dict_values['p_spec'] = request.form.get('p_spec')
            print(dict_values)
            contents, map_name = get_rank_info_and_map(dict_values)
            send_email(email, 'Your results have arrived!', contents, map_name)
            os.remove(map_name)
            return '''<!DOCTYPE html> <html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<title>Sent!</title>
</head>

<body>
<div class="container-fluid">
	<div class="row">
		<div style="width: 50%; margin: auto;">
			<h2>
				Form Submitted!
			</h2>
			<p>
				Check your email for your results. To view your customized, interactive map, download the attached map.html file and open it.
			</p>
			<form action="https://therapisthelp.wordpress.com">
				<input class="btn btn-outline-info btn-lg btn-block" type="submit" value="Return to Therapist Help" />
			</form>
		</div>
	</div>
</div>
</body>

</html>'''
        except Exception as e:
            print(e)
            return '<p>There was an error processing your request</p>'


    return '''

<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body class="nimbus-is-editor">'<form class="" method="POST">
  <ul>
    <li><label for="namel">Name:  </label>
    <input type="text" name="name" value=""></li>
    <li><label for="emaill">Email:  </label>
    <input type="text" name="email" value=""></li>
    <li><label for="adsressl">Address:  </label><input type="text" name="address" value=""></li>
  </ul>
  <p><b>
    Qualifications
  </b></p>

  <select class="" name="qualifications">
    <option value="therapist">Therapist</option>
    <option value="counseler">Counseler</option>
    <option value="psychologist">Psychologist</option>
  </select>
  <ul>
    <p><b>
      Insurance
    </b>
    </p>
  <li><select class="" name="insurance">
    <option value="Aetna">Aetna</option>
<option value="Aetna EAP">Aetna EAP</option>
<option value="Alliance">Alliance</option>
<option value="American Behavioral">American Behavioral</option>
<option value="Anthem">Anthem</option>
<option value="BCBS Blue Home UNC Alliance">BCBS Blue Home UNC Alliance</option>
<option value="BCBS Healthy Blue Medicaid">BCBS Healthy Blue Medicaid</option>
<option value="BCBS SHP">BCBS SHP</option>
<option value="Beacon">Beacon</option>
<option value="Blue Care">Blue Care</option>
<option value="Blue Care Network">Blue Care Network</option>
<option value="Blue Cross">Blue Cross</option>
<option value="Blue Home/UNC Health Alliance">Blue Home/UNC Health Alliance</option>
<option value="Blue Options">Blue Options</option>
<option value="Blue Select">Blue Select</option>
<option value="Blue Shield">Blue Shield</option>
<option value="Blue Value">Blue Value</option>
<option value="Blue Value/Blue Value w/UNC HA">Blue Value/Blue Value w/UNC HA</option>
<option value="BlueCross and BlueShield">BlueCross and BlueShield</option>
<option value="Cameron &amp; Associates">Cameron &amp; Associates</option>
<option value="CareFirst">CareFirst</option>
<option value="Ceridian">Ceridian</option>
<option value="Cigna">Cigna</option>
<option value="Classic Blue">Classic Blue</option>
<option value="ComPsych">ComPsych</option>
<option value="Coventry">Coventry</option>
<option value="E4 Health">E4 Health</option>
<option value="E4Health">E4Health</option>
<option value="Federal BCBS">Federal BCBS</option>
<option value="First Health">First Health</option>
<option value="Harvard Pilgrim">Harvard Pilgrim</option>
<option value="Health Advocate">Health Advocate</option>
<option value="Health Choice">Health Choice</option>
<option value="Health Net">Health Net</option>
<option value="HRI/Harris Rothenburg International">HRI/Harris Rothenburg International</option>
<option value="Humana">Humana</option>
<option value="Image Net EAP">Image Net EAP</option>
<option value="Magellan">Magellan</option>
<option value="MCMS">MCMS</option>
<option value="MedCost">MedCost</option>
<option value="Medicaid">Medicaid</option>
<option value="Medicare">Medicare</option>
<option value="MHN">MHN</option>
<option value="MultiPlan">MultiPlan</option>
<option value="NC State Health Plan">NC State Health Plan</option>
<option value="New Directions">New Directions</option>
<option value="Optum">Optum</option>
<option value="Out of Network">Out of Network</option>
<option value="PHCS">PHCS</option>
<option value="Piedmont employee assistance program">Piedmont employee assistance program</option>
<option value="SAS EAP provider">SAS EAP provider</option>
<option value="Self-pay">Self-pay</option>
<option value="Sliding scale">Sliding scale</option>
<option value="State Health Plan">State Health Plan</option>
<option value="TRICARE">TRICARE</option>
<option value="Tricare - Non Network Provider">Tricare - Non Network Provider</option>
<option value="UMR">UMR</option>
<option value="UNC Student Health Insurance">UNC Student Health Insurance</option>
<option value="UNC Student Health Insurance Plan">UNC Student Health Insurance Plan</option>
<option value="UnitedHealthcare">UnitedHealthcare</option>
<option value="Workplace Options EAP">Workplace Options EAP</option>
  </select></li>
  <p><b>
    Cost
  </b></p>
  <ul>
    <li><label for="minl">Min cost:  </label>
    <input type="text" name="min_cost" value=""></li>
    <li><label for="maxl">Max cost:  </label>
    <input type="text" name="max_cost" value=""></li>
  </ul>
  <p><b>
    Speciality
  </b>
  </p><li>
    <div class="grid-container">
    <div class="grid-item">
      <ul>
 <li><input type="checkbox" name="specialities" value="Addiction">Addiction</li>
    <li><input type="checkbox" name="specialities" value="ADHD">ADHD</li>
    <li><input type="checkbox" name="specialities" value="Anger Management">Anger Management</li>
    <li><input type="checkbox" name="specialities" value="Anxiety">Anxiety</li>
    <li><input type="checkbox" name="specialities" value="Autism">Autism</li>
    <li><input type="checkbox" name="specialities" value="Behavioral Issues">Behavioral Issues</li>
    <li><input type="checkbox" name="specialities" value="Bipolar Disorder">Bipolar Disorder</li>
    <li><input type="checkbox" name="specialities" value="Career Counseling">Career Counseling</li>
    <li><input type="checkbox" name="specialities" value="Child or Adolescent">Child or Adolescent</li>
    <li><input type="checkbox" name="specialities" value="Chronic Illness">Chronic Illness</li>
    <li><input type="checkbox" name="specialities" value="Chronic Pain">Chronic Pain</li>
    <li><input type="checkbox" name="specialities" value="Codependency">Codependency</li>
    <li><input type="checkbox" name="specialities" value="Coping Skills">Coping Skills</li>
    <li><input type="checkbox" name="specialities" value="Depression">Depression</li>
    <li><input type="checkbox" name="specialities" value="Developmental Disorders">Developmental Disorders</li>
    <li><input type="checkbox" name="specialities" value="Divorce">Divorce</li>
    <li><input type="checkbox" name="specialities" value="Dual Diagnosis">Dual Diagnosis</li>
    <li><input type="checkbox" name="specialities" value="Eating Disorders">Eating Disorders</li>
    <li><input type="checkbox" name="specialities" value="Emotional Disturbance">Emotional Disturbance</li>
    <li><input type="checkbox" name="specialities" value="Family Conflict">Family Conflict</li>
    <li><input type="checkbox" name="specialities" value="Gay">Gay</li>
    <li><input type="checkbox" name="specialities" value="Grief">Grief</li>
    <li><input type="checkbox" name="specialities" value="Infertility">Infertility</li>
    <li><input type="checkbox" name="specialities" value="Life Coaching">Life Coaching</li>
    <li><input type="checkbox" name="specialities" value="life satisfaction">life satisfaction</li>
    <li><input type="checkbox" name="specialities" value="Life Transitions">Life Transitions</li>
    <li><input type="checkbox" name="specialities" value="Marital and Premarital">Marital and Premarital</li>
    <li><input type="checkbox" name="specialities" value="Mood Disorders">Mood Disorders</li>
    <li><input type="checkbox" name="specialities" value="Parenting">Parenting</li>
  </ul>
  </div>
    <div class="grid-item">
      <ul>

    <li><input type="checkbox" name="specialities" value="Peer Relationships">Peer Relationships</li>
    <li><input type="checkbox" name="specialities" value="Personality Disorders">Personality Disorders</li>
    <li><input type="checkbox" name="specialities" value="Postpartum">Postpartum</li>
    <li><input type="checkbox" name="specialities" value="Prenatal">Prenatal</li>
    <li><input type="checkbox" name="specialities" value="Psychosis">Psychosis</li>
    <li><input type="checkbox" name="specialities" value="purpose">purpose</li>
    <li><input type="checkbox" name="specialities" value="Racial Identity">Racial Identity</li>
    <li><input type="checkbox" name="specialities" value="Relationship Issues">Relationship Issues</li>
    <li><input type="checkbox" name="specialities" value="School Issues">School Issues</li>
    <li><input type="checkbox" name="specialities" value="Self Esteem">Self Esteem</li>
    <li><input type="checkbox" name="specialities" value="Sex Therapy">Sex Therapy</li>
    <li><input type="checkbox" name="specialities" value="Sexual Abuse">Sexual Abuse</li>
    <li><input type="checkbox" name="specialities" value="Sexual Addiction">Sexual Addiction</li>
    <li><input type="checkbox" name="specialities" value="Sleep or Insomnia">Sleep or Insomnia</li>
    <li><input type="checkbox" name="specialities" value="Spirituality">Spirituality</li>
    <li><input type="checkbox" name="specialities" value="Sports Performance">Sports Performance</li>
    <li><input type="checkbox" name="specialities" value="Stress">Stress</li>
    <li><input type="checkbox" name="specialities" value="Substance Use">Substance Use</li>
    <li><input type="checkbox" name="specialities" value="Suicidal Ideation">Suicidal Ideation</li>
    <li><input type="checkbox" name="specialities" value="Testing and Evaluation">Testing and Evaluation</li>
    <li><input type="checkbox" name="specialities" value="Transgende">Transgender</li>
    <li><input type="checkbox" name="specialities" value="Trauma and PTSD">Trauma and PTSD</li>
    <li><input type="checkbox" name="specialities" value="Weight Loss">Weight Loss</li>
    <li><input type="checkbox" name="specialities" value="adult childrens relsps with paren">adult childrens relsps with paren</li>
    <li><input type="checkbox" name="specialities" value="Aspergers Syndrome">Aspergers Syndrome</li>
    <li><input type="checkbox" name="specialities" value="Mens Issues">Mens Issues</li>
    <li><input type="checkbox" name="specialities" value="Womens Issues">Womens Issues</li>
  </ul>
  </div>
    </div>
  </li>
  <p><b>
    Therapy type
  </b>
  </p>
  <ul>



  <div class="grid-container">
      <div class="grid-item">
        <li><input type="checkbox" name="approach" value="Art Therapy">Art Therapy</li>
<li><input type="checkbox" name="approach" value="Attachment-based">Attachment-based</li>
<li><input type="checkbox" name="approach" value="Biofeedback">Biofeedback</li>
<li><input type="checkbox" name="approach" value="Clinical Supervision and Licensed Supervisors -">Clinical Supervision and Licensed Supervisors -</li>
<li><input type="checkbox" name="approach" value="Coaching">Coaching</li>
<li><input type="checkbox" name="approach" value="Cognitive Behavioral (CBT)">Cognitive Behavioral (CBT)</li>
<li><input type="checkbox" name="approach" value="Culturally Sensitive">Culturally Sensitive</li>
<li><input type="checkbox" name="approach" value="Dialectical (DBT)">Dialectical (DBT)</li>
<li><input type="checkbox" name="approach" value="Eclectic">Eclectic</li>
<li><input type="checkbox" name="approach" value="EMDR">EMDR</li>
<li><input type="checkbox" name="approach" value="Emotionally Focused">Emotionally Focused</li>
<li><input type="checkbox" name="approach" value="Existential">Existential</li>
<li><input type="checkbox" name="approach" value="Experiential Therapy">Experiential Therapy</li>
<li><input type="checkbox" name="approach" value="Expressive Arts">Expressive Arts</li>
<li><input type="checkbox" name="approach" value="Family / Marital">Family / Marital</li>
<li><input type="checkbox" name="approach" value="Family Systems">Family Systems</li>
<li><input type="checkbox" name="approach" value="Feminist">Feminist</li>
<li><input type="checkbox" name="approach" value="Forensic Psychology">Forensic Psychology</li>
<li><input type="checkbox" name="approach" value="Gestalt">Gestalt</li>
<li><input type="checkbox" name="approach" value="Gottman Method">Gottman Method</li>
<li><input type="checkbox" name="approach" value="Humanistic">Humanistic</li>
<li><input type="checkbox" name="approach" value="Hypnotherapy">Hypnotherapy</li>
<li><input type="checkbox" name="approach" value="Imago">Imago</li>
<li><input type="checkbox" name="approach" value="Integrative">Integrative</li>
<li><input type="checkbox" name="approach" value="Internal Family Systems (IFS)">Internal Family Systems (IFS)</li>
<li><input type="checkbox" name="approach" value="Interpersonal">Interpersonal</li>
<li><input type="checkbox" name="approach" value="Intervention">Intervention</li>
<li><input type="checkbox" name="approach" value="Jungian">Jungian</li>
<li><input type="checkbox" name="approach" value="Mindfulness-Based (MBCT)">Mindfulness-Based (MBCT)</li>
<li><input type="checkbox" name="approach" value="Motivational Interviewing">Motivational Interviewing</li>
<li><input type="checkbox" name="approach" value="Multicultural">Multicultural</li>
<li><input type="checkbox" name="approach" value="Narrative">Narrative</li>

<li><input type="checkbox" name="approach" value="Neurofeedback">Neurofeedback</li>
<li><input type="checkbox" name="approach" value="Parent-Child Interaction (PCIT)">Parent-Child Interaction (PCIT)</li>
</div>
<div class="grid-item">
<li><input type="checkbox" name="approach" value="Person-Centered">Person-Centered</li>
<li><input type="checkbox" name="approach" value="Play Therapy">Play Therapy</li>
<li><input type="checkbox" name="approach" value="Positive Psychology">Positive Psychology</li>
<li><input type="checkbox" name="approach" value="Prolonged Exposure Therapy">Prolonged Exposure Therapy</li>
<li><input type="checkbox" name="approach" value="Psychoanalytic">Psychoanalytic</li>
<li><input type="checkbox" name="approach" value="Psychodynamic">Psychodynamic</li>
<li><input type="checkbox" name="approach" value="Psychological Testing and Evaluation">Psychological Testing and Evaluation</li>
<li><input type="checkbox" name="approach" value="Reality Therapy">Reality Therapy</li>
<li><input type="checkbox" name="approach" value="Relational">Relational</li>
<li><input type="checkbox" name="approach" value="Sandplay">Sandplay</li>
<li><input type="checkbox" name="approach" value="Solution Focused Brief (SFBT)">Solution Focused Brief (SFBT)</li>
<li><input type="checkbox" name="approach" value="Somatic">Somatic</li>
<li><input type="checkbox" name="approach" value="Strength-Based">Strength-Based</li>
<li><input type="checkbox" name="approach" value="Transpersonal">Transpersonal</li>
<li><input type="checkbox" name="approach" value="Trauma Focused">Trauma Focused</li>
</div>


    </div>
  </ul>
  </ul>
  <p><b>
    Priorities: How important is each category on a scale from 1 (not important) to 7 (very important)?
  </p></b>
  <ul>
    <li><label for="p_dist">Distance:  </label>
        <select class="" name="p_dist"?>
          <option value="1" name="1">1</option>
          <option value="2" name="2">2</option>
          <option value="3" name="3">3</option>
          <option value="4" name="4">4</option>
          <option value="5" name="5">5</option>
          <option value="6" name="6">6</option>
          <option value="7" name="7">7</option>
        </select>
    </li>
    <li><label for="p_qual">Qualifications:  </label>
        <select class="" name="p_qual"?>
          <option value="1" name="1">1</option>
          <option value="2" name="2">2</option>
          <option value="3" name="3">3</option>
          <option value="4" name="4">4</option>
          <option value="5" name="5">5</option>
          <option value="6" name="6">6</option>
          <option value="7" name="7">7</option>
        </select>
    </li>
    <li><label for="p_ins">Insurance:  </label>
        <select class="" name="p_ins"?>
          <option value="1" name="1">1</option>
          <option value="2" name="2">2</option>
          <option value="3" name="3">3</option>
          <option value="4" name="4">4</option>
          <option value="5" name="5">5</option>
          <option value="6" name="6">6</option>
          <option value="7" name="7">7</option>
        </select>
    </li>
    <li><label for="p_cst">Cost:  </label>
        <select class="" name="p_cst"?>
          <option value="1" name="1">1</option>
          <option value="2" name="2">2</option>
          <option value="3" name="3">3</option>
          <option value="4" name="4">4</option>
          <option value="5" name="5">5</option>
          <option value="6" name="6">6</option>
          <option value="7" name="7">7</option>
        </select>
    </li>
    <li><label for="p_spec">Speciality:  </label>
        <select class="" name="p_spec"?>
          <option value="1" name="1">1</option>
          <option value="2" name="2">2</option>
          <option value="3" name="3">3</option>
          <option value="4" name="4">4</option>
          <option value="5" name="5">5</option>
          <option value="6" name="6">6</option>
          <option value="7" name="7">7</option>
        </select>
    </li>
    <li><label for="p_type">Therapy Type:  </label>
        <select class="" name="p_type"?>
          <option value="1" name="1">1</option>
          <option value="2" name="2">2</option>
          <option value="3" name="3">3</option>
          <option value="4" name="4">4</option>
          <option value="5" name="5">5</option>
          <option value="6" name="6">6</option>
          <option value="7" name="7">7</option>
        </select>
    </li>
  </ul>


  <input type="submit" value="Submit">

</form>
<style media="screen">
  form {
    /* Center the form on the page */
    margin: 0 auto;
    width: 600px;
    /* Form outline */
    padding: 1em;
    border: 1px solid #CCC;
    border-radius: 1em;
  }

  ul {
    list-style: none;
    padding: 0;
    margin: 0;
    justify-content: start;


  }

  form li + li {
    list-style: none;
    margin-top: 1em;
      justify-content: space-evenly;
      justify-content: start;

  }

  label {
    /* Uniform size & alignment */
    display: inline-block;
    width: 90px;
    text-align: right;
  }
  input.text{
    width: 700px;
  }
  textarea{
    width: 700px;
  }
  .grid-container{
    display :grid;
    grid-template-columns: auto auto;
     justify-content: start;
     grid-column-gap: 50px;

  }
  .grid-item{
    grid-column-gap: 50px;
  }
'''
if __name__ == '__main__':
    print("starting")
    app.run(debug=True,
            host="0.0.0.0",
            port=8888,
            ssl_context='adhoc')
