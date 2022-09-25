class Valid:
  def __init__(self, name, data, options):
    self.name = name
    self.data = data
    self.errors = []
    self.required = options.get('required') if options.get('required') else None
    self.whitelist = options.get('whitelist') if options.get('whitelist') else None
    self.min_length = options.get('min_length') if options.get('min_length') else None
    self.max_length = options.get('max_length') if options.get('max_length') else None
    self.is_name = options.get('is_name') if options.get('is_name') else None
    self.is_email = options.get('is_email') if options.get('is_email') else None
    self.validate()

  def valid_required(self):
    if len(self.data) == 0:
      self.errors.append(f'{self.name} is required')

  def valid_min_length(self):
    if len(self.data) < self.min_length:
      self.errors.append(f'{self.name} must contain a minimum of {self.min_length} characters')

  def valid_max_length(self):
    if len(self.data) > self.max_length:
      self.errors.append(f'{self.name} can contain a maxiumum of {self.max_length} characters')

  def valid_whitelist(self):
    found = bool
    for x in self.data:
      if found == False: 
        self.errors.append(f'{self.name} contains illegal character')
        break
      found = False
      for y in self.whitelist:
        if (x == y): found = True

  def format_email(self):
    self.data = self.data.lower()
    self.data = self.data.strip()

  def validate(self):
    if self.min_length != None:
      self.valid_min_length()
    if self.max_length != None:
      self.valid_max_length()
    if self.required == True:
      self.valid_required()
    if self.whitelist != None:
      self.valid_whitelist()
    if self.is_name == True:
      self.valid_name()
    if self.is_email == True:
      self.format_email()
    



