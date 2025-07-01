# 📊 Task 6 – Password Strength Results

**Objective:** Evaluate different passwords using strength analysis tools and compare their estimated crack times.

---

## 🔐 Password Test Results (HowSecureIsMyPassword.net)

| Screenshot | Password (Hidden) | Estimated Time to Crack |
|------------|-------------------|--------------------------|
| ![](./screenshots/Screenshot%20From%202025-07-01%2020-26-47.png) | ★★★★★★★★★★★★ | **1 month** |
| ![](./screenshots/Screenshot%20From%202025-07-01%2020-27-16.png) | ★★★★★★★★★★★★ | **3 weeks** |
| ![](./screenshots/Screenshot%20From%202025-07-01%2020-27-43.png) | ★★★★★★★★★★★★★★★★★★★★ | **500 quadrillion years** |
| ![](./screenshots/Screenshot%20From%202025-07-01%2020-28-03.png) | ★★★★★★★★★★★★★★★★★★★★★★ | **3 sextillion years** |

---

## 🔐 Password Test Results (Bitwarden/NordPass)

| Screenshot | Password Tested     | Strength    | Estimated Crack Time    |
|------------|----------------------|-------------|--------------------------|
| ![](./screenshots/Screenshot%20From%202025-07-01%2020-33-38.png) | `password123`            | ❌ Very Weak | Less than a second |
| ![](./screenshots/Screenshot%20From%202025-07-01%2020-33-54.png) | `Pass@2024`              | ⚠️ Weak      | 41 minutes          |
| ![](./screenshots/Screenshot%20From%202025-07-01%2020-34-04.png) | `!M3nT0r$2024#SecuR3`    | ✅ Strong     | Centuries           |
| ![](./screenshots/Screenshot%20From%202025-07-01%2020-34-17.png) | `T#7n!9e@L$zQ%v*2025pX` | ✅ Strong     | Centuries           |

---

## 🧠 Observation

- Short/simple passwords like `password123` are crackable in less than a second.
- Slightly complex passwords like `Pass@2024` may still fall in minutes.
- Strong passwords with symbols, length, and randomness like `T#7n!9e@L$zQ%v*2025pX` are virtually uncrackable.

---

**Next Steps:**  
- Add these screenshots inside the `screenshots/` folder of your GitHub repo.
- Link this `results.md` in your `README.md` using `[📊 View Results](./results.md)`.

Let me know if you want a zipped repo or help pushing this to GitHub via CLI. ✅
