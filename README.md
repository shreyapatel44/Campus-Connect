# Campus Connect

**Campus Connect** is a comprehensive platform designed to streamline event management and university club administration. With intuitive tools for creating, updating, and managing clubs and events, Campus Connect empowers students and university staff to foster engagement and organize campus life efficiently.

## Features

- **Event Management**:  
  - Create, edit, and delete campus events  
  - RSVP, attendee management  
  - Event calendar view

- **University Club CRUD System**:  
  - Create, view, update, and delete university clubs  
  - Manage club members and profiles  
  - Post announcements and updates

- **User Authentication**  
  - Secure login and access controls for clubs and event organizers

- **Responsive Dashboard**  
  - Easy navigation for students, club admins, and event organizers

## Technologies Used

- Frontend: (e.g. React, Redux, Bootstrap)
- Backend: (e.g. Node.js, Express)
- Database: (e.g. MongoDB, PostgreSQL)
- Authentication: (e.g. JWT, OAuth)
- Others: (Specify as per project)

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/shreyapatel44/Campus-Connect.git
   cd Campus-Connect
   ```

2. **Install dependencies:**
   ```sh
   npm install
   # or, for backend/frontend separately
   cd client && npm install
   cd ../server && npm install
   ```

3. **Configure environment variables:**
   - Create a `.env` file in the root and specify necessary variables (e.g. DB connection string, JWT secret).

4. **Run the development server:**
   ```sh
   npm start
   # or: 
   cd client && npm start
   cd ../server && npm run dev
   ```

5. **Open [http://localhost:3000](http://localhost:3000) in your browser.**

## Usage

- **Register/Login:**  
  Access different features according to user roles (student, club admin).
- **Manage Clubs:**  
  Add, edit, remove clubs, manage club details.
- **Manage Events:**  
  Organize events, send invitations, track attendees.

## Contribution

Contributions are welcome! Please fork the repo, create a pull request, and follow conventional commit guidelines.

1. Fork this repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a pull request

## License

[MIT](LICENSE)  
Feel free to use, modify, and distribute as per license terms.

---

**Campus Connect** — Empowering student engagement and community building.
