
# Pantry Insight

## Overview

**Pantry Insight** is a web application designed to help users manage their pantry items efficiently. Users can add, remove, and update pantry items, search for recipes based on available ingredients, and get recipe suggestions. The application is built using **Next.js** for the frontend, **Firebase** for the backend, and integrates with the **Edamam Recipe Search API**. Google Sign-In is also integrated to allow users to authenticate with their Google accounts.

## Features

- **Pantry Management:** Add, remove, and update pantry items.
- **Search and Filter:** Easily search for items in the pantry.
- **Recipe Suggestions:** Find recipes based on the ingredients you have.
- **Google Sign-In:** Secure user authentication using Google accounts.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Deployment:** Deployed on Vercel with CI/CD integration.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Next.js)
- **Backend:** Firebase (Firestore for database)
- **Recipe API:** Edamam Recipe Search API
- **Authentication:** Google Sign-In

## Installation

To set up the Pantry Tracker project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pantry-tracker.git
   cd pantry-tracker
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Set up Firebase:**
   - Create a Firebase project and enable Firestore and Authentication.
   - Obtain your Firebase configuration details and create a `.env.local` file in the root directory with the following structure:

     ```
     NEXT_PUBLIC_FIREBASE_API_KEY=your_api_key
     NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your_auth_domain
     NEXT_PUBLIC_FIREBASE_PROJECT_ID=your_project_id
     NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your_storage_bucket
     NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
     NEXT_PUBLIC_FIREBASE_APP_ID=your_app_id
     ```

4. **Run the application:**

   ```bash
   npm run dev
   ```

5. **Access the application:**
   
   Open your web browser and navigate to `http://localhost:3000`.

## Usage

### Manage Pantry Items

- Access the pantry management page to add, remove, or update items.
- Utilize the search functionality to find specific items quickly.

### Find Recipes

- Go to the recipe finder page to search for recipes based on available ingredients.
- View recipe details including ingredients and instructions.

### Sign In with Google

- Use the Google Sign-In button on the login page to authenticate and access your account.

## File Structure

```
PantryTracker/
│
├── static/
│   ├── google-logo.png        # Logo image for the application.
│   ├── logo.ico               # Favicon for the website.
│   ├── logo.jpg               # Additional logo image.
│   ├── main_styles.css        # Main CSS styles for the application.
│   ├── manage_styles.css      # Styles specific to management pages.
│   └── styles.css             # General styles for all pages.
│
├── templates/
│   ├── forgot_password.html    # Page for password recovery.
│   ├── index.html              # Main landing page of the application.
│   ├── login.html              # Login page with Google Sign-In option.
│   ├── manage.html             # Page for managing pantry items.
│   ├── recipe_finder.html      # Page for finding recipes based on ingredients.
│   └── signup.html             # User registration page.
│
├── LICENSE                      # License file detailing project distribution terms.
├── README.md                    # Documentation file providing an overview of the project.
├── app.py                       # Main application file running Flask server (if applicable).
├── forms.html                  # HTML form templates used in various pages.
├── requirements.txt            # List of Python dependencies (if applicable).
└── .env.local                  # Environment variables configuration file (not included in version control).
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Edamam** for providing the Recipe Search API.
- **Google** for the authentication service.
