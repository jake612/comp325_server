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
            contents, map_name = get_rank_info_and_map(dict_values)
            send_email(email, 'Your results have arrived!', contents, map_name)
            os.remove(map_name)
            return '<p>Message Sent!</p>'
        except Exception as e:
            print(e)
            return '<p>There was an error processing your request</p>'


    return '''
    '<form class="" method="POST">
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
    <option value="  Aetna">Aetna</option>
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
<option value="Cameron & Associates">Cameron & Associates</option>
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
  <p>
  </p>
  <ul>
    <li><label for="minl">Min cost:  </label>
    <input type="text" name="min_cost" value=""></li>
    <li><label for="maxl">Max cost:  </label>
    <input type="text" name="max_cost" value=""></li>
  </ul>
  <p><b>
    Speciality
  </b>
  <li>
    <div class="grid-container">
      <div class="grid-item">
        <ul>

    <li><input type="checkbox" name="Addiction" value="">Addiction</li>
    <li><input type="checkbox" name="ADHD" value="">ADHD</li>
    <li><input type="checkbox" name="Anger Management" value="">Anger Management</li>
    <li><input type="checkbox" name="Anxiety" value="">Anxiety</li>
    <li><input type="checkbox" name="Autism" value="">Autism</li>
    <li><input type="checkbox" name="Behavioral Issues" value="">Behavioral Issues</li>
    <li><input type="checkbox" name="Bipolar Disorder" value="">Bipolar Disorder</li>
    <li><input type="checkbox" name="Career Counseling" value="">Career Counseling</li>
    <li><input type="checkbox" name="Child or Adolescent" value="">Child or Adolescent</li>
    <li><input type="checkbox" name="Chronic Illness" value="">Chronic Illness</li>
    <li><input type="checkbox" name="Chronic Pain" value="">Chronic Pain</li>
    <li><input type="checkbox" name="Codependency" value="">Codependency</li>
    <li><input type="checkbox" name="Coping Skills" value="">Coping Skills</li>
    <li><input type="checkbox" name="Depression" value="">Depression</li>
    <li><input type="checkbox" name="Developmental Disorders" value="">Developmental Disorders</li>
    <li><input type="checkbox" name="Divorce" value="">Divorce</li>
    <li><input type="checkbox" name="Dual Diagnosis" value="">Dual Diagnosis</li>
    <li><input type="checkbox" name="Eating Disorders" value="">Eating Disorders</li>
    <li><input type="checkbox" name="Emotional Disturbance" value="">Emotional Disturbance</li>
    <li><input type="checkbox" name="Family Conflict" value="">Family Conflict</li>
    <li><input type="checkbox" name="Gay" value="">Gay</li>
    <li><input type="checkbox" name="Grief" value="">Grief</li>
    <li><input type="checkbox" name="Infertility" value="">Infertility</li>
    <li><input type="checkbox" name="Life Coaching" value="">Life Coaching</li>
    <li><input type="checkbox" name="life satisfaction" value="">life satisfaction</li>
    <li><input type="checkbox" name="Life Transitions" value="">Life Transitions</li>
    <li><input type="checkbox" name="Marital and Premarital" value="">Marital and Premarital</li>
    <li><input type="checkbox" name="Mood Disorders" value="">Mood Disorders</li>
    <li><input type="checkbox" name="Parenting" value="">Parenting</li>
  </ul>
  </div>
    <div class="grid-item">
      <ul>

    <li><input type="checkbox" name="Peer Relationships" value="">Peer Relationships</li>
    <li><input type="checkbox" name="Personality Disorders" value="">Personality Disorders</li>
    <li><input type="checkbox" name="Postpartum" value="">Postpartum</li>
    <li><input type="checkbox" name="Prenatal" value="">Prenatal</li>
    <li><input type="checkbox" name="Psychosis" value="">Psychosis</li>
    <li><input type="checkbox" name="purpose" value="">purpose</li>
    <li><input type="checkbox" name="Racial Identity" value="">Racial Identity</li>
    <li><input type="checkbox" name="Relationship Issues" value="">Relationship Issues</li>
    <li><input type="checkbox" name="School Issues" value="">School Issues</li>
    <li><input type="checkbox" name="Self Esteem" value="">Self Esteem</li>
    <li><input type="checkbox" name="Sex Therapy" value="">Sex Therapy</li>
    <li><input type="checkbox" name="Sexual Abuse" value="">Sexual Abuse</li>
    <li><input type="checkbox" name="Sexual Addiction" value="">Sexual Addiction</li>
    <li><input type="checkbox" name="Sleep or Insomnia" value="">Sleep or Insomnia</li>
    <li><input type="checkbox" name="Spirituality" value="">Spirituality</li>
    <li><input type="checkbox" name="Sports Performance" value="">Sports Performance</li>
    <li><input type="checkbox" name="Stress" value="">Stress</li>
    <li><input type="checkbox" name="Substance Use" value="">Substance Use</li>
    <li><input type="checkbox" name="Suicidal Ideation" value="">Suicidal Ideation</li>
    <li><input type="checkbox" name="Testing and Evaluation" value="">Testing and Evaluation</li>
    <li><input type="checkbox" name="Transgender" value="">Transgender</li>
    <li><input type="checkbox" name="Trauma and PTSD" value="">Trauma and PTSD</li>
    <li><input type="checkbox" name="Weight Loss" value="">Weight Loss</li>
    <li><input type="checkbox" name="adult childrens relsps with paren" value="">adult childrens relsps with paren</li>
    <li><input type="checkbox" name="Aspergers Syndrome" value="">Aspergers Syndrome</li>
    <li><input type="checkbox" name="Mens Issues" value="">Mens Issues</li>
    <li><input type="checkbox" name="Womens Issues" value="">Womens Issues</li>
  </ul>
  </div>
    </div>
  </li>
  <p><b>
    Therpay type
  </b>
  </p>
  <ul>
    <div class="grid-container">
      <div class="grid-item">
        <li><input type="checkbox" name="  Art Therapy" value="">  Art Therapy</li>
<li><input type="checkbox" name="  Attachment-based" value="">  Attachment-based</li>
<li><input type="checkbox" name="  Biofeedback" value="">  Biofeedback</li>
<li><input type="checkbox" name="  Clinical Supervision and Licensed Supervisors -" value="">  Clinical Supervision and Licensed Supervisors -</li>
<li><input type="checkbox" name="  Coaching" value="">  Coaching</li>
<li><input type="checkbox" name="  Cognitive Behavioral (CBT)" value="">  Cognitive Behavioral (CBT)</li>
<li><input type="checkbox" name="  Culturally Sensitive" value="">  Culturally Sensitive</li>
<li><input type="checkbox" name="  Dialectical (DBT)" value="">  Dialectical (DBT)</li>
<li><input type="checkbox" name="  Eclectic" value="">  Eclectic</li>
<li><input type="checkbox" name="  EMDR" value="">  EMDR</li>
<li><input type="checkbox" name="  Emotionally Focused" value="">  Emotionally Focused</li>
<li><input type="checkbox" name="  Existential" value="">  Existential</li>
<li><input type="checkbox" name="  Experiential Therapy" value="">  Experiential Therapy</li>
<li><input type="checkbox" name="  Expressive Arts" value="">  Expressive Arts</li>
<li><input type="checkbox" name="  Family / Marital" value="">  Family / Marital</li>
<li><input type="checkbox" name="  Family Systems" value="">  Family Systems</li>
<li><input type="checkbox" name="  Feminist" value="">  Feminist</li>
<li><input type="checkbox" name="  Forensic Psychology" value="">  Forensic Psychology</li>
<li><input type="checkbox" name="  Gestalt" value="">  Gestalt</li>
<li><input type="checkbox" name="  Gottman Method" value="">  Gottman Method</li>
<li><input type="checkbox" name="  Humanistic" value="">  Humanistic</li>
<li><input type="checkbox" name="  Hypnotherapy" value="">  Hypnotherapy</li>
<li><input type="checkbox" name="  Imago" value="">  Imago</li>
<li><input type="checkbox" name="  Integrative" value="">  Integrative</li>
<li><input type="checkbox" name="  Internal Family Systems (IFS)" value="">  Internal Family Systems (IFS)</li>
<li><input type="checkbox" name="  Interpersonal" value="">  Interpersonal</li>
<li><input type="checkbox" name="  Intervention" value="">  Intervention</li>
<li><input type="checkbox" name="  Jungian" value="">  Jungian</li>
<li><input type="checkbox" name="  Mindfulness-Based (MBCT)" value="">  Mindfulness-Based (MBCT)</li>
<li><input type="checkbox" name="  Motivational Interviewing" value="">  Motivational Interviewing</li>
<li><input type="checkbox" name="  Multicultural" value="">  Multicultural</li>
<li><input type="checkbox" name="  Narrative" value="">  Narrative</li>

<li><input type="checkbox" name="  Neurofeedback" value="">  Neurofeedback</li>
<li><input type="checkbox" name="  Parent-Child Interaction (PCIT)" value="">  Parent-Child Interaction (PCIT)</li>
</div>
<div class="grid-item">
<li><input type="checkbox" name="  Person-Centered" value="">  Person-Centered</li>
<li><input type="checkbox" name="  Play Therapy" value="">  Play Therapy</li>
<li><input type="checkbox" name="  Positive Psychology" value="">  Positive Psychology</li>
<li><input type="checkbox" name="  Prolonged Exposure Therapy" value="">  Prolonged Exposure Therapy</li>
<li><input type="checkbox" name="  Psychoanalytic" value="">  Psychoanalytic</li>
<li><input type="checkbox" name="  Psychodynamic" value="">  Psychodynamic</li>
<li><input type="checkbox" name="  Psychological Testing and Evaluation" value="">  Psychological Testing and Evaluation</li>
<li><input type="checkbox" name="  Reality Therapy" value="">  Reality Therapy</li>
<li><input type="checkbox" name="  Relational" value="">  Relational</li>
<li><input type="checkbox" name="  Sandplay" value="">  Sandplay</li>
<li><input type="checkbox" name="  Solution Focused Brief (SFBT)" value="">  Solution Focused Brief (SFBT)</li>
<li><input type="checkbox" name="  Somatic" value="">  Somatic</li>
<li><input type="checkbox" name="  Strength-Based" value="">  Strength-Based</li>
<li><input type="checkbox" name="  Transpersonal" value="">  Transpersonal</li>
<li><input type="checkbox" name="  Trauma Focused" value="">  Trauma Focused</li>
<li><input type="checkbox" name=" Adlerian" value=""> Adlerian</li>
<li><input type="checkbox" name=" Art Therapy" value=""> Art Therapy</li>
<li><input type="checkbox" name=" Attachment-based" value=""> Attachment-based</li>
<li><input type="checkbox" name=" Biofeedback" value=""> Biofeedback</li>
<li><input type="checkbox" name=" Clinical Supervision and Licensed Supervisors -" value=""> Clinical Supervision and Licensed Supervisors -</li>
<li><input type="checkbox" name=" Coaching" value=""> Coaching</li>
<li><input type="checkbox" name=" Cognitive Behavioral (CBT)" value=""> Cognitive Behavioral (CBT)</li>
<li><input type="checkbox" name=" Culturally Sensitive" value=""> Culturally Sensitive</li>
<li><input type="checkbox" name=" Dialectical (DBT)" value=""> Dialectical (DBT)</li>
<li><input type="checkbox" name=" Eclectic" value=""> Eclectic</li>
<li><input type="checkbox" name=" EMDR" value=""> EMDR</li>
<li><input type="checkbox" name=" Existential" value=""> Existential</li>
<li><input type="checkbox" name=" Family / Marital" value=""> Family / Marital</li>
<li><input type="checkbox" name=" Humanistic" value=""> Humanistic</li>
<li><input type="checkbox" name=" Hypnotherapy" value=""> Hypnotherapy</li>
<li><input type="checkbox" name=" Neurofeedback" value=""> Neurofeedback</li>
<li><input type="checkbox" name=" Psychoanalytic" value=""> Psychoanalytic</li>
<li><input type="checkbox" name=" treatment-approach" value=""> treatment-approach</li>
<li><input type="checkbox" name="Acceptance and Commitment (ACT)" value="">Acceptance and Commitment (ACT)</li>
</div>


    </div>
  </ul>

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

</style>'''

if __name__ == '__main__':
    print("starting")
    app.run(debug=True,
            host="0.0.0.0",
            port=8888)
