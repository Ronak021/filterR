document.addEventListener('DOMContentLoaded', () => {
    const filterTypeSelect = document.getElementById('filter-type');
    const columnNameSelect = document.getElementById('column-name');
    const filterConditionSelect = document.getElementById('filter-condition');
    
    const columnOptions = {
        integer: ['id', 'age', 'salary', 'projectsCompleted'],
        string: ['name', 'role', 'department', 'accessLevel', 'lastLogin'],
        date: ['hireDate'],
        boolean: ['isActive']
    };
    
    const conditionOptions = {
        integer: ['equals', 'lessThan', 'lessThanOrEqual', 'greaterThan', 'greaterThanOrEqual', 'range', 'notEqual'],
        string: ['contains', 'notContains', 'equals', 'notEqual', 'startsWith', 'endsWith', 'isNull', 'isNotNull'],
        date: ['dateIs', 'dateRange', 'equals', 'lessThan', 'lessThanOrEqual', 'greaterThan', 'greaterThanOrEqual', 'notEqual', 'isNull', 'isNotNull'],
        boolean: ['equals', 'isNull', 'isNotNull']
    };

    filterTypeSelect.addEventListener('change', () => {
        const selectedType = filterTypeSelect.value;
        const columns = columnOptions[selectedType] || [];
        const conditions = conditionOptions[selectedType] || [];

    
        columnNameSelect.innerHTML = columns.map(column => `<option value="${column}">${column}</option>`).join('');

        
        filterConditionSelect.innerHTML = conditions.map(condition => `<option value="${condition}">${condition}</option>`).join('');
    });
});
