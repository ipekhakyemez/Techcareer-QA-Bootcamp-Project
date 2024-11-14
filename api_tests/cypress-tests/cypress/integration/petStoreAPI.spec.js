describe('Petstore API Tests', () => {
 
    it('Get Pet Details (GET)', () => {
      cy.request({
        method: 'GET',
        url: 'https://petstore.swagger.io/v2/pet/1', 
      }).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.have.property('id', 1);
      });
    });
  
    it('Add a New Pet (POST)', () => {
      const newPet = {
        id: 123,
        name: 'Fluffy',
        status: 'available',
      };
  
      cy.request({
        method: 'POST',
        url: 'https://petstore.swagger.io/v2/pet',
        body: newPet,
        headers: {
          'Content-Type': 'application/json',
        },
      }).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.have.property('name', 'Fluffy');
        expect(response.body).to.have.property('status', 'available');
      });
    });
  
    it('Update Pet Details (PUT)', () => {
      const updatedPet = {
        id: 12345,
        name: 'Fluffy Updated',
        status: 'sold',
      };
  
      cy.request({
        method: 'PUT',
        url: 'https://petstore.swagger.io/v2/pet',
        body: updatedPet,
        headers: {
          'Content-Type': 'application/json',
        },
      }).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.have.property('name', 'Fluffy Updated');
        expect(response.body).to.have.property('status', 'sold');
      });
    });
  
    it('Delete Pet (DELETE)', () => {
      const petId = 123;
  
      cy.request({
        method: 'DELETE',
        url: `https://petstore.swagger.io/v2/pet/${petId}`,
      }).then((response) => {
        expect(response.status).to.eq(200);
      });
    });
  
    it('Check Deleted Pet (GET)', () => {
      const petId = 123;
  
      cy.request({
        method: 'GET',
        url: `https://petstore.swagger.io/v2/pet/${petId}`,
        failOnStatusCode: false,
      }).then((response) => {
        expect(response.status).to.eq(404);
        expect(response.body).to.have.property('message', 'Pet not found');
      });
    });
  });
  