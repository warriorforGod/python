current_users = ['billy','betty','randy','julie','timmy']

new_users = ['randy','julie']

for user in new_users:
	if user.lower() in current_users:
		print("\nUsername unavailable.  Please choose a new username.")
	else:
		print("\nUsername is available.")
