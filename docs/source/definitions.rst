Definitions
===================================

There are several terms and concepts that the GLYN CMS relies on. These terms are presented here.

| Terms       | Definitions |
| ----------- | ----------- |
| CMS         | Abbreviation for “Content Management System”. A CMS is software that helps manage the creation and modification of digital content, such as articles, images, videos, and documents.       |
| Django      | Django is a free and open-source software library written in Python that is used to create web applications.        |
| Wagtail     | Wagtail is a free and open-source CMS for Django.       |
| GLYN Wagtail CMS     | GLYN uses Wagtail, Django, and plenty of custom code to deploy a website that can scale from feature phones all the way to desktops. Throughout this documentation, this software solution will be referred to as “the GLYN Wagtail CMS”, or more simply as “the CMS”.       |
| Dashboard | The initial view immediately after logging into the CMS. Displays the Pages, Images, Documents, and Media files currently loaded on the site, as well as your recently edited Pages and any Pages that are awaiting review. |
| Page | In the GLYN Wagtail CMS, the Page is the simplest form of presenting content. There are different variations of the Page. Each has different use cases. See “Page Types” below for a list of different Page variations. |
| Page Types | Pages can be any one of the following: <ol><li>Homepage</li><li>Standard page</li><li>Organisation page</li><li>Blog page</li><li>Event page</li><li>Resource page</li></ol> |
| Homepage | This is the content on the landing page located at http://greatlakesyouth.africa. All other pages on the website are descendants of this page. Since the website is in multiple languages, there are different homepages (for english, french and swahili) each with its own tree of child pages |
| Standard page | A standard page is used to create general content pages for example FAQs. They have no structure and all their formatting can be done in the editor. Examples include: Privay Policy page |
| Organisation page | Organisation pages are used to create youth initiatives. All information on the organisation can be added through this interface. All organisations will be found on the **Organisation Index page: Youth initiatives**
| Blog page | Blog pages are used to create articles usually known as blogs. They primarily consist of a title, excerpt, editor, featured image, video and galleries. Blog pages are a child pages under the **Blog index page: Newsroom** |
| Event page | Event pages are necessary to create upcoming events or even add events already passed and other relevant information. These appear on the **Event Index page: Events**
| Resource page | Resource pages are essentially documents. Documents for public use can be uploaded and properly tagged. These will show up on the **Resource Index (Library) page**  |

Index Pages
===================================

We have mentioned index pages a lot in the Definitions section. Index Pages are special types of Pages that can only exist as the direct child of a Homepage. Index Pages are similar to folders on your operating system, but can only contain one type of Child Page. For example, all blogs will go into a Blog Index Page. Similarly, all events will go into a Events Index Page. All organisations go into a Organisation Index Page. Sites are typically organized as Homepage -> Index Page -> Pages 
