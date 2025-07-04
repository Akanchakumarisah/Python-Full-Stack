# HTML Tables Notes

HTML Tables are used to display data in a structured, tabular format, such as rows and columns, making it easier to organize and present information like schedules, product lists, or comparison charts.

---

## What Are HTML Tables?

HTML Tables organize data into rows and columns, similar to a spreadsheet. Each table cell contains data, and tables are often used for data presentation, though modern web design favors CSS for layout purposes.

**Common Uses**:
- Displaying tabular data (e.g., student grades, price lists).
- Creating structured layouts (though CSS is preferred for this).

---

## Basic Structure of an HTML Table

The `<table>` element is the container for all table-related elements. It consists of rows (`<tr>`), header cells (`<th>`), and data cells (`<td>`).

**Basic Example**:
```html
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>20</td>
    </tr>
</table>
```

### Key Elements:
- **`<table>`**: Defines the table.
- **`<tr>`**: Defines a table row.
- **`<th>`**: Defines a header cell (bold and centered by default).
- **`<td>`**: Defines a data cell.

---

## Table Structure with Headings and Body

For better organization and accessibility, tables can use `<thead>`, `<tbody>`, and `<tfoot>` to group rows.

**Example**:
```html
<table>
    <thead>
        <tr>
            <th>Product</th>
            <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Laptop</td>
            <td>$999</td>
        </tr>
        <tr>
            <td>Phone</td>
            <td>$499</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>Total</td>
            <td>$1498</td>
        </tr>
    </tfoot>
</table>
```

### Key Elements:
- **`<thead>`**: Groups header rows.
- **`<tbody>`**: Groups main content rows.
- **`<tfoot>`**: Groups footer rows (e.g., totals).

---

## Spanning Rows and Columns

To merge cells across rows or columns:
- **`rowspan`**: Spans a cell across multiple rows.
- **`colspan`**: Spans a cell across multiple columns.

**Example**:
```html
<table>
    <tr>
        <th>Category</th>
        <th colspan="2">Details</th>
    </tr>
    <tr>
        <td rowspan="2">Electronics</td>
        <td>Laptop</td>
        <td>$999</td>
    </tr>
    <tr>
        <td>Phone</td>
        <td>$499</td>
    </tr>
</table>
```

---

## Table Attributes

Attributes enhance table functionality or styling (though CSS is preferred for styling):
- **`border`**: Adds a border (e.g., `border="1"` for a visible border, though CSS is better).
- **`id`/`class`**: For styling or JavaScript.
- **`scope`**: Improves accessibility for `<th>` (e.g., `scope="col"` or `scope="row"`).

**Example**:
```html
<table border="1">
    <tr>
        <th scope="col">Name</th>
        <th scope="col">Grade</th>
    </tr>
    <tr>
        <td scope="row">Bob</td>
        <td>A</td>
    </tr>
</table>
```

---

## Accessibility in Tables

To make tables accessible to screen readers:
- Use `<th>` with `scope` to clarify headers.
- Add a `<caption>` to describe the table’s purpose.
- Use `id` and `headers` attributes for complex tables.

**Example**:
```html
<table>
    <caption>Student Grades</caption>
    <tr>
        <th scope="col">Name</th>
        <th scope="col">Grade</th>
    </tr>
    <tr>
        <td>Bob</td>
        <td>A</td>
    </tr>
</table>
```

---

## Best Practices

- Use tables **only for tabular data**, not layouts (use CSS for layouts).
- Include `<thead>`, `<tbody>`, and `<tfoot>` for semantic structure.
- Add `<caption>` for clarity.
- Use `scope` for accessible headers.
- Style tables with CSS for better control (e.g., borders, spacing).

---

## Practice Exercises

1. Create a table with 3 rows and 2 columns, including headers.
2. Build a table with a `<thead>`, `<tbody>`, and `<tfoot>` for a product price list.
3. Use `rowspan` or `colspan` to merge cells in a table.
4. Add a `<caption>` and `scope` attributes to a table for accessibility.

---