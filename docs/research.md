About rst metadata directive: https://docutils.sourceforge.io/docs/ref/rst/directives.html#metadata
Writing custom HTML metadata: https://stackoverflow.com/questions/10533764/best-practice-for-meta-data-in-a-html-document

```html
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" class="">
<head>
    <meta name="application-name" content="Our app name" 
        data-details="52:AS6[rxSdsMd4RgYXJgeabsRAVBZ:0406139009]" 
        data-policyId="1234567890"
        data-partyId="0987654321"
        data-emailAddress="user@email.com"
        data-error="49"
        data-subsessionid="bffd5bc0-a03e-42e5-a531-50529dae57e3"
    />
</head>
```
For more info read: http://www.whatwg.org/specs/web-apps/current-work/multipage/elements.html#custom-data-attribute

Metadata Document title: https://docutils.sourceforge.io/docs/ref/rst/directives.html#metadata-document-title

Example:

**RST Code**

```rst
.. meta::
   :application-name data-policyId=1234567890: sphinx-pdf-generate
```

**Output:**

```html
<meta content="sphinx-pdf-generate" data-policyid="1234567890" name="application-name">
```

**JS to access metadata**

```js
var sphinx_pdf_generate_meta = document.querySelector("meta[content='sphinx-pdf-generate']");
let _policyid = sphinx_pdf_generate_meta.getAttribute('data-policyid');
let _subsessionid = sphinx_pdf_generate_meta.getAttribute('data-subsessionid');
```