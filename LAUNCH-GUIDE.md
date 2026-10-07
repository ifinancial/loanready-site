# Loan Ready powered by iFinancial: Launch Guide

## What's in this package
- `site/`: the full website, 22 pages plus a thank-you page and a 404 page. Upload this folder.
- `build.py`: the source the pages are generated from, for future edits.

## Hosting: Netlify (free)
Netlify is recommended because it is free, fast, includes free SSL, and handles the Free Loan Score form with no extra software.

1. Go to app.netlify.com and sign up with admin@goifinancial.com.
2. Click **Add new site → Deploy manually**, then drag the `site` folder onto the page. The site is live in about 30 seconds on a temporary netlify.app address.
3. Go to **Site configuration → Domain management → Add a domain** and enter `loanready.goifinancial.com`.
4. Log in wherever goifinancial.com's DNS is managed (your registrar or WordPress host). Add a **CNAME** record:
   - Name: `loanready`
   - Value: your-site-name.netlify.app (Netlify shows the exact value)
5. Wait for DNS to update (minutes to a few hours). Netlify then issues SSL automatically.
6. Form notifications: go to **Forms → loan-score → Form notifications** and add an email notification to info@goifinancial.com (and Danny or the sales team). Submissions also appear in the Netlify dashboard.

Your main goifinancial.com WordPress site does not change.

## After it's live (week 1)
1. **Google Search Console**: add `loanready.goifinancial.com`, verify through DNS, and submit `/sitemap.xml`.
2. **Google Business Profile**: use ONE profile for the 751 Northlake Blvd Suite 2D address. If iFinancial already has a profile there, add Loan Ready services to it rather than creating a second listing at the same address. Duplicate listings get suspended.
3. **Google Analytics (GA4)**: create a property and paste the tag into each page's `<head>`. Or ask Claude to add it and rebuild.
4. **Link from goifinancial.com**: point the "Credit Repair" menu item on the main site to this site.

## Before you promote it
- [ ] Get **written permission** from P.C., J.D., S.M. and C.G. to share their results (initials only). Remove any client who won't sign.
- [ ] Have your attorney review the billing language (paid after work is performed) and the contract against CROA, Florida Ch. 817 Part III, and the Telemarketing Sales Rule.
- [ ] Confirm the $10,000 Florida credit service organization bond is in place.
- [ ] Remove "NO ONE GETS DENIED!" and "guaranteed success" from goifinancial.com. Guarantee language is a regulator red flag in credit repair.
- [ ] Consider a local 561 phone number for the site and Google profile. It helps local rankings and call-through. The main site also lists a different number (866-232-2858) in its FAQ, so use one number everywhere.
- [ ] Add real photos of the office, signage and team to the Visit Us page.

## Making changes
Edit the text in `build.py` and run `python3 build.py`, then drag the `site` folder onto Netlify again under **Deploys**. Or ask Claude to make the change and send you a new package.

## Blogs
The blog section is not linked yet, so no empty pages are published. Once your writer delivers posts, they go under `/blog/`, link to the matching service and loan pages, and get added to the sitemap.
