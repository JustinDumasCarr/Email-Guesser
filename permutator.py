class Permutator:


  # Checks self.nickName for existance and uniqueness against firstName
  # When deciding whether or not to make email permutations with it.
  def checkNN(self, formula):
    if self.nickName != "" and self.nickName != self.firstName:
      self.emailOutput.append(formula)



  # Checks nickInitial for existance and uniqueness against firstInitial
  # when deciding whether or not to make email permutations with it.
  def checkNI(self, formula):
    if self.nickInitial != "" and self.nickInitial != self.firstInitial:
        self.emailOutput.append(formula)



  # Checks that Middle Initial exists
  def checkMidIn(self, formula):
    if self.middleInitial != "":
        self.emailOutput.append(formula)



  # Checks that Middle Name Exists
  def checkMidNam(self, formula):
    if  self.middleName  != "" and  self.middleName  != self.middleInitial:
        self.emailOutput.append(formula)



  # Checks that nickInitial exists and != firstInitial, and that Middle Initial exists
  def checkNIandMI(self, formula):
    if self.nickInitial != "" and self.nickInitial != self.firstInitial and self.middleInitial != "":
        self.emailOutput.append(formula)



  # Checks that self.nickName exists and != firstName, and that Middle Initial Exists
  def checkNNandMI(self, formula):
    if self.nickName != "" and self.nickName !=  self.firstName  and self.middleInitial != "":
        self.emailOutput.append(formula)



  # Checks that self.nickName exists and != firstName, and that Middle Name Exists and != middleInitial
  def checkNNandMN(self, formula):
    if self.nickName != "" and self.nickName !=  self.firstName  and  self.middleName  != "" and  self.middleName  != self.middleInitial:
        self.emailOutput.append(formula)



  # Most Common Emails, including self.nickName and nickInitial Variations
  # self.nickName versions check for existance
  # nickInitial versions chck for existance and uniqueness against firstInitial
  def commonEmails(self, theDomain):
    emailEnder = "@" + theDomain

    self.emailOutput.append(self.firstName + emailEnder); # First Name
    self.checkNN(self.nickName + emailEnder); # Nick Name
    self.emailOutput.append(self.lastName + emailEnder); # {ln}
    self.emailOutput.append(self.firstName +  self.lastName  + emailEnder); # {fn}{ln}
    self.checkNN(self.nickName +  self.lastName  + emailEnder); # {nn}{ln}
    self.emailOutput.append(self.firstName + "." +  self.lastName  + emailEnder); # {fn}.{ln}
    self.checkNN(self.nickName + "." +  self.lastName  + emailEnder); # {nn}.{ln}
    self.emailOutput.append(self.firstInitial +  self.lastName  + emailEnder); # {fi}{ln}
    self.checkNI(self.nickInitial +  self.lastName  + emailEnder); # {ni}{ln}
    self.emailOutput.append(self.firstInitial + "." +  self.lastName  + emailEnder); # {fi}.{ln}
    self.checkNI(self.nickInitial + "." +  self.lastName  + emailEnder); # {ni}.{ln}
    self.emailOutput.append(self.firstName + self.lastInitial + emailEnder); # {fn}{li}
    self. checkNN(self.nickName + self.lastInitial + emailEnder); # {nn}{li}
    self. emailOutput.append(self.firstName + "." + self.lastInitial + emailEnder); # {fn}.{li}
    self. checkNN(self.nickName + "." + self.lastInitial + emailEnder); # {nn}.{li}
    self. emailOutput.append(self.firstInitial + self.lastInitial + emailEnder); # {fi}{li}
    self.checkNI(self.nickInitial + self.lastInitial + emailEnder); # {ni}{li}
    self.emailOutput.append(self.firstInitial + "." + self.lastInitial + emailEnder); # {fi}.{li}
    self.checkNI(self.nickInitial + "." + self.lastInitial + emailEnder); # {ni}.{li}


  # Email Permutations that begin with last names
  def lessCommonEmails(self, theDomain):
    emailEnder = "@" + theDomain

    self.emailOutput.append(self.lastName +  self.firstName  + emailEnder); # {ln}{fn}
    self.checkNN(self.lastName + self.nickName + emailEnder); # {ln}{nn}
    self.emailOutput.append(self.lastName + "." +  self.firstName  + emailEnder); # {ln}.{fn}
    self.checkNN(self.lastName + "." + self.nickName + emailEnder); # {ln}.{nn}
    self.emailOutput.append(self.lastName + self.firstInitial + emailEnder); # {ln}{fi}
    self.checkNI(self.lastName + self.nickInitial + emailEnder); # {ln}{ni}
    self.emailOutput.append(self.lastName + "." + self.firstInitial + emailEnder); # {ln}.{fi}
    self.checkNI(self.lastName + "." + self.nickInitial + emailEnder); # {ln}.{ni}
    self.emailOutput.append(self.lastInitial +  self.firstName  + emailEnder); # {li}{fn}
    self.checkNN(self.lastInitial + self.nickName + emailEnder); # {li}{nn}
    self.emailOutput.append(self.lastInitial + "." +  self.firstName  + emailEnder); # {li}.{fn}
    self.checkNN(self.lastInitial + "." + self.nickName + emailEnder); # {li}.{nn}
    self. emailOutput.append(self.lastInitial + self.firstInitial + emailEnder); # {li}{fi}
    self.checkNI(self.lastInitial + self.nickInitial + emailEnder); # {li}{ni}
    self.emailOutput.append(self.lastInitial + "." + self.firstInitial + emailEnder); # {li}.{fi}
    self.checkNI(self.lastInitial + "." + self.nickInitial + emailEnder); # {li}.{ni}


  # Emails that contain middle names and initials
  def middleEmails(self, theDomain):
    emailEnder = "@" + theDomain

    self.checkMidIn(self.firstInitial + self.middleInitial +  self.lastName  + emailEnder); # {fi}{mi}{ln}
    self.checkNIandMI(self.nickInitial + self.middleInitial +  self.lastName  + emailEnder); # {ni}{mi}{ln}
    self.checkMidIn(self.firstInitial + self.middleInitial + "." +  self.lastName  + emailEnder); # {fi}{mi}.{ln}
    self.checkNIandMI(self.nickInitial + self.middleInitial + "." +  self.lastName  + emailEnder); # {ni}{mi}.{ln}
    self.checkMidIn(self.firstName + self.middleInitial +  self.lastName  + emailEnder); # {fn}{mi}{ln}
    self.checkNNandMI(self.nickName + self.middleInitial +  self.lastName  + emailEnder); # {nn}{mi}{ln}
    self.checkMidIn(self.firstName + "." + self.middleInitial + "." +  self.lastName  + emailEnder); # {fn}.{mi}.{ln}
    self.checkNNandMI(self.nickName + "." + self.middleInitial + "." +  self.lastName  + emailEnder); # {nn}.{mi}.{ln}
    self.checkMidNam(self.firstName +  self.middleName  +  self.lastName  + emailEnder); # {fn}{mn}{ln}
    self.checkNNandMN(self.nickName +  self.middleName  +  self.lastName  + emailEnder); # {nn}{mn}{ln}
    self.checkMidNam(self.firstName + "." +  self.middleName  + "." +  self.lastName  + emailEnder); # {fn}.{mn}.{ln}
    self.checkNNandMN(self.nickName + "." +  self.middleName  + "." +  self.lastName  + emailEnder); # {nn}.{mn}.{ln}


  # Emails using dashes
  def dashEmails(self, theDomain):
    emailEnder = "@" + theDomain

    self.emailOutput.append(self.firstName + "-" +  self.lastName  + emailEnder); # {fn}-{ln}
    self.checkNN(self.nickName + "-" +  self.lastName  + emailEnder); # {nn}-{ln}
    self.emailOutput.append(self.firstInitial + "-" +  self.lastName  + emailEnder); # {fi}-{ln}
    self.checkNI(self.nickInitial + "-" +  self.lastName  + emailEnder); # {ni}-{ln}
    self.emailOutput.append(self.firstName + "-" + self.lastInitial + emailEnder); # {fn}-{li}
    self.checkNN(self.nickName + "-" + self.lastInitial + emailEnder); # {nn}-{li}
    self.emailOutput.append(self.firstInitial + "-" + self.lastInitial + emailEnder); # {fi}-{li}
    self.checkNI(self.nickInitial + "-" + self.lastInitial + emailEnder); # {ni}-{li}
    self.emailOutput.append(self.lastName + "-" +  self.firstName  + emailEnder); # {ln}-{fn}
    self.checkNN(self.lastName + "-" + self.nickName + emailEnder); # {ln}-{nn}
    self.emailOutput.append(self.lastName + "-" + self.firstInitial + emailEnder); # {ln}-{fi}
    self.checkNI(self.lastName + "-" + self.nickInitial + emailEnder); # {ln}-{ni}
    self.emailOutput.append(self.lastInitial + "-" +  self.firstName  + emailEnder); # {li}-{fn}
    self.checkNN(self.lastInitial + "-" + self.nickName + emailEnder); # {li}-{nn}
    self.emailOutput.append(self.lastInitial + "-" + self.firstInitial + emailEnder); # {li}-{fi}
    self.checkNI(self.lastInitial + "-" + self.nickInitial + emailEnder); # {li}-{ni}
    self.checkMidIn(self.firstInitial + self.middleInitial + "-" +  self.lastName  + emailEnder); # {fi}{mi}-{ln}
    self.checkNIandMI(self.nickInitial + self.middleInitial + "-" +  self.lastName  + emailEnder); # {ni}{mi}-{ln}
    self.checkMidIn(self.firstName + "-" + self.middleInitial + "-" +  self.lastName  + emailEnder); # {fn}-{mi}-{ln}
    self.checkNNandMI(self.nickName + "-" + self.middleInitial + "-" +  self.lastName  + emailEnder); # {nn}-{mi}-{ln}
    self.checkMidNam(self.firstName + "-" +  self.middleName  + "-" +  self.lastName  + emailEnder); # {fn}-{mn}-{ln}
    self.checkNNandMN(self.nickName + "-" +  self.middleName  + "-" +  self.lastName  + emailEnder); # {nn}-{mn}-{ln}


  # Emails using Underscores
  def underscoreEmails(self, theDomain):
    emailEnder = "@" + theDomain

    self.emailOutput.append(self.firstName + "_" +  self.lastName  + emailEnder); # {fn}_{ln}
    self.checkNN(self.nickName + "_" +  self.lastName  + emailEnder); # {nn}_{ln}
    self.emailOutput.append(self.firstInitial + "_" +  self.lastName  + emailEnder); # {fi}_{ln}
    self.checkNI(self.nickInitial + "_" +  self.lastName  + emailEnder); # {ni}_{ln}
    self.emailOutput.append(self.firstName + "_" + self.lastInitial + emailEnder); # {fn}_{li}
    self.checkNN(self.nickName + "_" + self.lastInitial + emailEnder); # {nn}_{li}
    self.emailOutput.append(self.firstInitial + "_" + self.lastInitial + emailEnder); # {fi}_{li}
    self.checkNI(self.nickInitial + "_" + self.lastInitial + emailEnder); # {ni}_{li}
    self.emailOutput.append(self.lastName + "_" +  self.firstName  + emailEnder); # {ln}_{fn}
    self.checkNN(self.lastName + "_" + self.nickName + emailEnder); # {ln}_{nn}
    self.emailOutput.append(self.lastName + "_" + self.firstInitial + emailEnder); # {ln}_{fi}
    self.checkNI(self.lastName + "_" + self.nickInitial + emailEnder); # {ln}_{ni}
    self.emailOutput.append(self.lastInitial + "_" +  self.firstName  + emailEnder); # {li}_{fn}
    self.emailOutput.append(self.lastInitial + "_" + self.firstInitial + emailEnder); # {li}_{fi}
    self.checkNI(self.lastInitial + "_" + self.nickInitial + emailEnder); # {li}_{ni}
    self.checkMidIn(self.firstInitial + self.middleInitial + "_" +  self.lastName  + emailEnder); # {fi}{mi}_{ln}
    self.checkNIandMI(self.nickInitial + self.middleInitial + "_" +  self.lastName  + emailEnder); # {ni}{mi}_{ln}
    self.checkMidIn(self.firstName + "_" + self.middleInitial + "_" +  self.lastName  + emailEnder); # {fn}_{mi}_{ln}
    self.checkNNandMI(self.nickName + "_" + self.middleInitial + "_" +  self.lastName  + emailEnder); # {nn}_{mi}_{ln}
    self.checkMidNam(self.firstName + "_" +  self.middleName  + "_" +  self.lastName  + emailEnder); # {fn}_{mn}_{ln}
    self.checkNNandMN(self.nickName + "_" +  self.middleName  + "_" +  self.lastName  + emailEnder); # {nn}_{mn}_{ln}


  def permute(self, firstName,lastName,nickName,middleName,domain1,domain2,domain3):
    # Make sure the Array is empty, in case this is run multiple times
    self.emailOutput = []

    # Put the form field data into variables
    self.firstName  = firstName.lower()
    if firstName:
     self.firstInitial = firstName[0]
    else: self.firstInitial = ""
    self.lastName  = lastName.strip().lower()
    if lastName:
     self.lastInitial = lastName[0]
    else: self.lastInitial = ""

    self.nickName = nickName.strip().lower()
    if nickName:
     self.nickInitial = nickName[0]
    else: self.nickInitial = ""
    self.middleName  = middleName.strip().lower()
    if middleName:
     self.middleInitial = middleName[0]
    else: self.middleInitial = ""
    self.domain1 = domain1.strip().lower()
    self.domain2 = domain2.strip().lower()
    self.domain3 = domain3.strip().lower()

    # Run each category of email permutation for each domain
    self.commonEmails(self.domain1)
    if self.domain2 != "":
      self.commonEmails(self.domain2)

    if self.domain3 != "":
      self.commonEmails(self.domain3)


    self.lessCommonEmails(self.domain1)
    if self.domain2 != "":
      self.lessCommonEmails(self.domain2)

    if self.domain3 != "":
      self.lessCommonEmails(self.domain3)


    self.middleEmails(self.domain1)
    if self.domain2 != "":
      self.middleEmails(self.domain2)

    if self.domain3 != "":
      self.middleEmails(self.domain3)


    self.dashEmails(self.domain1)
    if self.domain2 != "":
      self.dashEmails(self.domain2)

    if self.domain3 != "":
      self.dashEmails(self.domain3)


    self.underscoreEmails(self.domain1)
    if self.domain2 != "":
      self.underscoreEmails(self.domain2)

    if self.domain3 != "":
      self.underscoreEmails(self.domain3)


    return self.emailOutput


