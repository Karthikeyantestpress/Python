class Developer:
  def check_pass_fail(self):
    if self.mark>=40:
        return True
    else :
        return False

Developer1=Developer()
Developer1.name ="Karthikeyan"
Developer1.platform ="Python"
Developer1.mark =90

Did_pass =Developer1.check_pass_fail()
print(Did_pass)

print(Developer1.name)
print(Developer1.platform)